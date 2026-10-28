# dean0x/skim

⭐ 30 · Rust · MIT · 推送 2026-09-29 · [GitHub](https://github.com/dean0x/skim) · [官网](https://dean0x.github.io/x/skim/) · 个人维护

**为编码 agent 优化上下文的 Rust CLI：代码压缩与输出瘦身**

面向 coding agent 用户的上下文优化工具：基于 AST 解析（tree-sitter，18 种语言）对源码做 6 级转换（15-95% 削减），并压缩测试、构建、lint、包管理器与 git 输出；通过 PreToolUse hook 将 cat/grep/git diff 等命令改写为 skim 等价物，支持 token 预算级联自动选择模式。另提供基于 git 历史的代码库热图（churn/blast radius/bus factor）与 AST 感知的代码搜索。以 Rust 二进制 CLI 提供，可经 cargo/brew/npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AST 解析 18 种语言、6 种转换模式（15-95% token 削减），3000 行约 14.6ms
- 命令改写 hook：将 cat/ls/grep/git diff 等改写为 skim 等价命令
- 测试/构建/lint/包管理器/git 输出压缩，带三级降级策略
- 基于 git 历史的代码库热图与 n-gram+AST 复合代码搜索

## 适用场景

- 把大代码库压缩到单条 prompt 内让 AI 解答架构问题
- 让 coding agent 自动消费瘦身后的命令输出以降低 token 消耗
- 识别高频变更、高修复风险的代码热点文件

## 场景标签

 · 领域:开发者工具/LLM 上下文优化

## 证据(README 行号)

> L5: Other tools filter terminal noise. Skim understands your code. It parses ASTs across 18 languages, strips implementa
> L54: - PreToolUse hook rewrites `ls`, `grep`, `gh`, `cargo test`, `vitest`, `git diff` into skim equivalents
> L63: - `skim cargo test`, `skim pytest`, `skim vitest`, `skim jest`, `skim go test`

## 星数曲线

```mermaid
xychart-beta
    title "dean0x/skim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81e09982565c` · [字段定义](../../DATASET.md)*
