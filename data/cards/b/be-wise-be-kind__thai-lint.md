# be-wise-be-kind/thai-lint

⭐ 25 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/be-wise-be-kind/thai-lint) · [官网](https://thai-lint.readthedocs.io/) · 组织维护

**多语言 linter：检测 AI 生成代码的常见反模式**

面向开发者的命令行代码检查工具，针对 AI 编码助手常引入的反模式提供 18 种 linter：重复代码、深层嵌套、魔法数字、性能反模式、SRP 违规、Rust 特有的 unwrap/clone 滥用等，覆盖 Python、TypeScript、JavaScript、Rust 并使用统一规则。支持 pip 安装、uvx 免安装运行与 Docker 镜像，提供 YAML/JSON/pyproject.toml 三级配置、行级/文件级忽略机制、GitHub Actions 集成与 --parallel 并行加速。需 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 种 linter 覆盖 Python/TypeScript/JavaScript/Rust 四种语言
- 检测 AI 工具常引入的反模式：重复代码、深嵌套、魔法数字、SRP 违规等
- 支持 .thailint.yaml/.thailint.json/pyproject.toml 三级配置与 5 级忽略机制
- 提供 Docker 镜像、CI/CD 集成与 --parallel 并行模式（多核下 2-4x 提速）

## 适用场景

- 检查 AI 编码助手生成的代码中的常见反模式
- 在 CI/CD 流水线中自动检测重复代码与深层嵌套
- 对 Rust 项目检测 unwrap/clone 滥用与异步阻塞调用

## 场景标签

 · 领域:软件开发/代码质量

## 证据(README 行号)

> L10: **The AI Linter** - Catch the mistakes AI coding assistants keep making.
> L12: thailint detects anti-patterns that AI tools frequently introduce: duplicate code, excessive nesting, magic numbers

## 星数曲线

```mermaid
xychart-beta
    title "be-wise-be-kind/thai-lint 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-30 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d3bd9e1e3219` · [字段定义](../../DATASET.md)*
