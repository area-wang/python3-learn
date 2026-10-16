# 11-Monorepo管理

> 从零搭建一个 Python monorepo：多个包 + 一个应用，共用一套依赖锁、一套工具链，又能各自独立构建和发布。

本章使用 **uv workspace** 作为主线工具。文中所有命令均在 uv 0.12 / Python 3.11 下实际跑通。

---

## 📑 目录

- [0. 先搞清楚：什么是 monorepo](#0-先搞清楚什么是-monorepo)
- [1. 工具选型](#1-工具选型)
- [2. 目标结构](#2-目标结构)
- [3. Step 1：准备环境](#3-step-1准备环境)
- [4. Step 2：创建工作区根目录](#4-step-2创建工作区根目录)
- [5. Step 3：创建成员包](#5-step-3创建成员包)
- [6. Step 4：编写代码并声明内部依赖](#6-step-4编写代码并声明内部依赖)
- [7. Step 5：安装与运行](#7-step-5安装与运行)
- [8. Step 6：统一开发工具链](#8-step-6统一开发工具链)
- [9. Step 7：组织测试](#9-step-7组织测试)
- [10. Step 8：管理第三方依赖](#10-step-8管理第三方依赖)
- [11. Step 9：构建与发布](#11-step-9构建与发布)
- [12. Step 10：任务入口与 CI](#12-step-10任务入口与-ci)
- [13. 常见坑](#13-常见坑)
- [14. 进阶方向](#14-进阶方向)
- [15. 学习路线清单](#15-学习路线清单)

---

## 0. 先搞清楚：什么是 monorepo

**Monorepo**：把多个相关的项目（库、服务、脚本）放在**同一个 Git 仓库**里管理。对立面是 polyrepo（一个项目一个仓库）。

| | Monorepo | Polyrepo |
|---|---|---|
| 跨项目改动 | 一个 PR 同时改库和使用方，原子提交 | 要拆成多个仓库的 PR，还要协调发版顺序 |
| 依赖版本 | 一把锁，全仓库一致 | 各仓库各锁各的，容易漂移 |
| 工具配置 | lint / 类型检查 / CI 配一次 | 每个仓库重复配 |
| 代码复用 | 内部包直接引用，无需先发布 | 必须先发布到包仓库才能被引用 |
| 代价 | 仓库变大；CI 要做"只跑受影响部分"；权限难细分 | 复用和同步成本高 |

**Python 里做 monorepo 要解决的 4 个核心问题：**

1. **内部包互相引用**：`api` 要能 `import utils`，且改了 `utils` 立刻生效（可编辑安装）。
2. **依赖统一解析**：所有包的第三方依赖放在一起求解，只有一个 `uv.lock`。
3. **共享工具链**：pytest / ruff / mypy 在根目录配置一次。
4. **独立构建发布**：每个包仍然是标准 Python 包，能单独 `build` 和 `publish`。

> 💡 **什么时候不该用**：只有一个项目、或各项目团队/发布节奏完全独立时，单仓库单项目更简单。

---

## 1. 工具选型

| 方案 | 特点 | 适用 |
|---|---|---|
| **uv workspace**（本章） | 原生支持、单一 lockfile、速度快、配置少 | 绝大多数中小型 Python monorepo，**首选** |
| Hatch | 支持多环境管理，monorepo 需配合 path 依赖 | 已在用 Hatch 的项目 |
| Poetry | 没有原生 workspace，通常靠 path 依赖 + 插件 | 存量 Poetry 项目 |
| Pants / Bazel | 增量构建、依赖图分析、远程缓存 | 几十上百个包、多语言的大型仓库 |
| 纯 pip + `pip install -e` | 无锁文件、手动维护安装顺序 | 仅用于理解原理 |

**学习建议**：先用 uv workspace 跑通完整流程，遇到"CI 太慢、包太多"再考虑 Pants。

---

## 2. 目标结构

本章要搭建的仓库（3 个成员：两个库 + 一个应用）：

```text
my-monorepo/
├── pyproject.toml          # 工作区根：声明成员、共享开发工具和配置
├── uv.lock                 # 整个仓库唯一的锁文件
├── .python-version         # 统一 Python 版本
├── packages/               # 可复用的库
│   ├── core/               # mono-core：最底层，无内部依赖
│   │   ├── pyproject.toml
│   │   ├── src/mono_core/
│   │   └── tests/
│   └── utils/              # mono-utils：依赖 mono-core
│       ├── pyproject.toml
│       ├── src/mono_utils/
│       └── tests/
└── apps/                   # 可运行的应用
    └── api/                # mono-api：依赖 mono-utils
        ├── pyproject.toml
        └── src/mono_api/
```

依赖方向（**只能单向，不能循环**）：

```text
mono-api  →  mono-utils  →  mono-core
```

**命名约定**（新手最容易混）：

- 发布名（`pyproject.toml` 里的 `name`）：`mono-core`，用连字符
- 导入名（`import` 时的包目录）：`mono_core`，用下划线
- 两者 uv 会自动对应，但你要清楚各自出现在哪

---

## 3. Step 1：准备环境

```bash
# 安装 uv（macOS）
brew install uv          # 或：curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version

# 不需要自己装 Python，uv 会按需下载。也可以手动指定：
uv python install 3.11
```

创建仓库：

```bash
mkdir my-monorepo && cd my-monorepo
git init
```

---

## 4. Step 2：创建工作区根目录

根目录是一个 **virtual workspace root**：它只负责声明"这里是工作区"，自身不是一个可安装的包。手写根 `pyproject.toml`：

```toml
# my-monorepo/pyproject.toml
[tool.uv.workspace]
members = ["packages/*", "apps/*"]
```

固定 Python 版本：

```bash
uv python pin 3.11      # 生成 .python-version
```

要点：

- `members` 支持 glob，之后在 `packages/` 或 `apps/` 下新增目录会自动成为成员。
- 根目录**没有** `[project]` 表，所以 `uv sync` 不会把根当作包安装，这正是我们想要的。

---

## 5. Step 3：创建成员包

用 `uv init` 在子目录里生成包骨架：

```bash
uv init --lib packages/core  --name mono-core     # 库：src 布局 + py.typed
uv init --lib packages/utils --name mono-utils
uv init --app apps/api       --name mono-api      # 应用
```

`--lib` 与 `--app` 的区别：

| | `--lib` | `--app` |
|---|---|---|
| 目的 | 被别人 import | 直接运行 |
| 生成 `py.typed` | 是（声明支持类型检查） | 否 |
| 入口脚本 | 无 | `[project.scripts]` 里有一个命令 |

执行后会发现：

1. 根 `pyproject.toml` 的 workspace 保持不变（用了 glob，已覆盖新成员）。
2. 每个成员目录里多了 `.python-version`、`README.md`、`pyproject.toml`、`src/<导入名>/`。
3. **清理**：成员里的 `.python-version` 删掉，统一用根目录那一份：

```bash
rm packages/*/.python-version apps/*/.python-version
```

> `uv init` 会从 git config 读取作者信息写进 `authors`，按需修改。

成员的 `pyproject.toml` 本身就是一个**完整、独立的 Python 项目配置**，例如 `packages/core/pyproject.toml`：

```toml
[project]
name = "mono-core"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["uv_build>=0.12.3,<0.13.0"]
build-backend = "uv_build"
```

---

## 6. Step 4：编写代码并声明内部依赖

### 6.1 写三层代码

```python
# packages/core/src/mono_core/__init__.py
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

```python
# packages/utils/src/mono_utils/__init__.py
from mono_core import greet


def shout(name: str) -> str:
    return greet(name).upper()
```

```python
# apps/api/src/mono_api/__init__.py
from mono_utils import shout


def main() -> None:
    print(shout("monorepo"))
```

### 6.2 声明依赖（关键一步）

**光写 `import` 不够**，必须在 `pyproject.toml` 里声明，否则环境里装不上。用命令声明：

```bash
uv add --package mono-utils mono-core    # utils 依赖 core
uv add --package mono-api   mono-utils   # api 依赖 utils
```

`--package` 表示"这条依赖加到哪个成员上"。uv 会自动改写 `packages/utils/pyproject.toml`：

```toml
[project]
dependencies = [
    "mono-core",
]

[tool.uv.sources]
mono-core = { workspace = true }
```

理解这两段的分工：

- `dependencies`：**标准的 Python 依赖声明**，会随包发布出去。
- `[tool.uv.sources]`：**uv 专用**，告诉 uv "`mono-core` 不要去 PyPI 找，用本工作区里的那个"。`workspace = true` 默认以**可编辑模式**安装，改源码立即生效。发布时这段不会带出去。

---

## 7. Step 5：安装与运行

```bash
uv sync --all-packages       # 安装所有成员 + 开发依赖，生成 uv.lock 和 .venv
```

> 因为根是 virtual root，必须用 `--all-packages` 才会安装全部成员；也可以只装某个成员及其依赖：`uv sync --package mono-api`。

运行应用：

```bash
uv run --package mono-api mono-api
# 输出：HELLO, MONOREPO!
```

三层调用链 `api → utils → core` 都生效了，且你修改任一层源码，重跑立刻看到变化。

常用命令速查：

| 命令 | 作用 |
|---|---|
| `uv sync --all-packages` | 装所有成员 |
| `uv sync --package <name>` | 只装某成员及其传递依赖 |
| `uv run --package <name> <cmd>` | 以某成员为上下文运行命令 |
| `uv tree` | 查看依赖树（含内部依赖） |
| `uv lock` | 重新解析并更新锁文件 |
| `uv lock --check` | 检查锁文件是否最新（CI 用） |

`uv tree` 的结果能直观验证依赖方向：

```text
mono-api v0.1.0
└── mono-utils v0.1.0
    └── mono-core v0.1.0
```

---

## 8. Step 6：统一开发工具链

开发工具（测试、lint、类型检查）**放在根目录**，所有成员共用。这是 monorepo 的核心收益之一。

把根 `pyproject.toml` 扩展为：

```toml
[tool.uv.workspace]
members = ["packages/*", "apps/*"]

# 开发依赖组：只在开发时安装，不会随任何包发布
[dependency-groups]
dev = [
    "pytest>=8",
    "ruff>=0.6",
    "mypy>=1.11",
]

[tool.pytest.ini_options]
testpaths = ["packages", "apps"]
addopts = "--import-mode=importlib"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]   # 错误、未使用、import 排序、现代语法、常见 bug

[tool.mypy]
strict = true
```

重新同步并运行：

```bash
uv sync --all-packages

uv run ruff check .            # lint
uv run ruff format .           # 格式化
uv run mypy packages apps      # 类型检查
uv run pytest                  # 测试（在仓库根跑，覆盖所有成员）
```

> 成员目录里**不需要**再各放一份 ruff / mypy 配置，工具会向上查找到根目录的配置。个别包要特殊规则时，再在该成员的 `pyproject.toml` 里加 `[tool.ruff]` 覆盖。

---

## 9. Step 7：组织测试

测试放在**各成员自己的 `tests/` 目录**，和被测代码一起移动、一起维护：

```text
packages/core/tests/test_greet.py
packages/utils/tests/test_shout.py
```

```python
# packages/utils/tests/test_shout.py
from mono_utils import shout


def test_shout() -> None:
    assert shout("a") == "HELLO, A!"
```

运行方式：

```bash
uv run pytest                                  # 全部
uv run pytest packages/utils                   # 只测某个成员
uv run --package mono-utils pytest packages/utils   # 只装该成员及依赖再测，更贴近真实环境
```

**为什么根配置里要 `--import-mode=importlib`？**
`tests/` 目录通常没有 `__init__.py`。默认导入模式下，不同成员里**同名的测试文件**（比如都叫 `test_models.py`）会冲突报 "import file mismatch"。`importlib` 模式按文件路径导入，避免这个问题。

---

## 10. Step 8：管理第三方依赖

给某个成员加第三方依赖：

```bash
uv add --package mono-core "pydantic>=2"
```

它只写进 `packages/core/pyproject.toml`，同时更新**唯一的** `uv.lock`。

核心规则：

1. **依赖写在用到它的成员里**，不要图省事全塞根目录。这样每个包发布时依赖声明才是准确的。
2. **只有一个 `uv.lock`**：不同成员对同一个库的版本要求必须能同时满足，否则 `uv lock` 会报冲突，强迫你在提交前解决，而不是线上才发现。
3. 常用命令：

```bash
uv lock --upgrade-package pydantic   # 只升级某一个依赖
uv lock --upgrade                    # 升级全部
uv remove --package mono-core pydantic
uv add --dev --package mono-core hypothesis   # 仅给某成员加开发依赖
```

4. 提交 `uv.lock` 到 Git，并在 CI 里用 `uv lock --check` 防止忘记更新。

---

## 11. Step 9：构建与发布

每个成员都是标准包，可以独立构建：

```bash
uv build --package mono-core       # 只构建一个，产物在 dist/
uv build --all-packages            # 构建全部
```

产物：

```text
dist/mono_core-0.1.0-py3-none-any.whl
dist/mono_core-0.1.0.tar.gz
...
```

发布到 PyPI（或私有源）：

```bash
uv publish                          # 需要配置 token，如环境变量 UV_PUBLISH_TOKEN
```

**发布前必做：给内部依赖加版本约束。**

`[tool.uv.sources]` 不会随包发布。别人从 PyPI 安装 `mono-utils` 时，看到的只是 `dependencies = ["mono-core"]`，没有版本下限。所以要手动写明：

```toml
[project]
dependencies = [
    "mono-core>=0.1.0",
]
```

**版本策略**（二选一，早定早好）：

- **统一版本**：所有包一起升级、同一个版本号。简单，适合紧密耦合的包。
- **独立版本**：各包各自语义化版本。灵活，但要仔细维护内部依赖的版本范围。

---

## 12. Step 10：任务入口与 CI

### 12.1 统一任务入口

把常用命令封装起来，新同事只需记住 `make xxx`：

```makefile
# Makefile
.PHONY: install lint format typecheck test check

install:
	uv sync --all-packages

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy packages apps

test:
	uv run pytest

check: lint typecheck test
```

> 也可以用 [just](https://github.com/casey/just) 或 `poethepoet`，思路相同。

### 12.2 CI 基本流程

CI 里每次执行的核心步骤（以 GitHub Actions 为例）：

```yaml
# .github/workflows/ci.yml
name: CI
on:
  pull_request:
  push:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6        # action 版本以官方文档为准
      - run: uv lock --check               # 锁文件必须是最新的
      - run: uv sync --all-packages --frozen
      - run: uv run ruff check .
      - run: uv run ruff format --check .
      - run: uv run mypy packages apps
      - run: uv run pytest
```

### 12.3 只跑受影响的部分（仓库变大后）

初期全量跑即可。包多了以后，可以用 `paths` 过滤，只在相关目录变动时触发对应任务：

```yaml
on:
  pull_request:
    paths:
      - "packages/core/**"
      - "pyproject.toml"
      - "uv.lock"
```

注意：改了 `core` 会影响所有依赖它的包，所以**下游也要一起测**。手工维护这种规则很容易漏，这正是 Pants / Bazel 这类工具存在的原因（见第 14 节）。

---

## 13. 常见坑

| 现象 | 原因 | 解决 |
|---|---|---|
| `ModuleNotFoundError: mono_core` | 只写了 `import`，没声明依赖，或没 sync | `uv add --package <调用方> <被依赖方>`，再 `uv sync --all-packages` |
| `uv sync` 后成员没装上 | 根是 virtual root，默认不装成员 | 加 `--all-packages` 或 `--package` |
| 发布后别人装不上 / 版本不对 | 内部依赖没写版本下限，`sources` 不随包发布 | 在 `dependencies` 里写 `mono-core>=x.y.z` |
| pytest 报 `import file mismatch` | 多个成员有同名测试文件 | 配 `--import-mode=importlib`，或给 `tests/` 加唯一命名 |
| 目录名和导入名对不上 | 发布名用 `-`，导入名用 `_` | `mono-core` ↔ `mono_core`，目录用 `src/mono_core/` |
| `uv lock` 报版本冲突 | 两个成员对同一库的要求互斥 | 统一约束范围；这是 monorepo 的"特性"，不是 bug |
| 循环依赖 | `core` 反过来 import `utils` | 重构：把共用部分下沉到更底层的包 |
| 每个成员各配一套 ruff / mypy | 没利用根目录配置 | 配置放根，成员只在确有特殊需要时覆盖 |
| `.venv` 或 `dist/` 被提交 | 缺少 `.gitignore` | 根目录加 `.gitignore`，至少含 `.venv/`、`dist/`、`__pycache__/` |

---

## 14. 进阶方向

学完基础流程后，可按需深入：

1. **变更检测**：根据 `git diff` 找出被修改的包，加上所有下游依赖，只测这些。可以先自己写脚本解析 `uv tree`，再评估是否引入 Pants。
2. **自动化版本和变更日志**：release-please、towncrier、python-semantic-release。
3. **Docker 构建**：只安装某个应用及其依赖，如 `uv sync --package mono-api --no-dev --frozen`，让镜像不含无关包。
4. **预提交钩子**：`pre-commit` 在提交前跑 ruff 与格式化。
5. **依赖约束统一**：用 `[tool.uv] constraint-dependencies` 在根目录统一限定某些库的版本范围。
6. **Pants / Bazel**：包数量到几十个、构建很慢时，用它们做依赖图分析和增量缓存。

---

## 15. 学习路线清单

按顺序完成，每步都能独立验证：

- [ ] 理解 monorepo 与 polyrepo 的取舍，能说出适用场景
- [ ] 安装 uv，创建仓库，写出 virtual workspace 根 `pyproject.toml`
- [ ] 用 `uv init --lib / --app` 创建 3 个成员
- [ ] 写出 `api → utils → core` 三层调用，`uv run` 跑通
- [ ] 能解释 `dependencies` 与 `[tool.uv.sources]` 各自的作用
- [ ] 在根目录配好 pytest / ruff / mypy，三条命令全绿
- [ ] 每个成员有自己的测试，`uv run pytest` 全部通过
- [ ] 给某个成员加第三方依赖，观察 `uv.lock` 变化
- [ ] `uv build --all-packages` 产出全部 wheel，并检查内部依赖版本下限
- [ ] 写出 Makefile 和一份 CI 配置
- [ ] 把已有的单项目（如仓库里的 `my-project`）迁入 `packages/` 变成成员

练习见 [练习题.md](./练习题.md)。

---

## 🔗 参考资料

- uv 官方文档 · Workspaces：<https://docs.astral.sh/uv/concepts/projects/workspaces/>
- uv 官方文档 · Dependencies：<https://docs.astral.sh/uv/concepts/projects/dependencies/>
- uv 官方文档 · Build & Publish：<https://docs.astral.sh/uv/guides/package/>
