# harmont-dev/harmont-cli

⭐ 21 · Rust · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/harmont-dev/harmont-cli) · [官网](https://harmont.dev) · 组织维护

**用 Python 定义 CI/CD 流水线的命令行工具，可本地 Docker 或云端运行**

面向开发者的 CI/CD 工具：以 Python（或 TypeScript）代码定义流水线，`hm run` 在本机 Docker 中执行与云端完全相同的流水线，内置确定性 Docker 层缓存与基于 DAG 的步骤并行。提供 Rust、Go、Python、Zig、C/C++ 等类型化工具链预设；`hm run --cloud` 将本地工作树提交到 Harmont Cloud 托管 runner，输出 NDJSON 事件流。AI 部分：`hm init` 可安装三个 Claude Code 技能，用于生成流水线、从 GitHub Actions 迁移和本地验证；去掉该功能流水线本身仍可独立使用。CLI 采用双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Python 流水线定义，本地 Docker 与云端运行结果逐字节一致
- 确定性 Docker 层缓存，仅重执行输入变化的步骤
- 基于 DAG 的并行执行与 `-k` 失败后继续运行
- `hm init` 安装 Claude Code 技能，支持生成流水线与 GitHub Actions 迁移

## 适用场景

- 在本地完整跑 CI 流水线，推送前发现失败
- 把 GitHub Actions 的 YAML 流水线迁移为 Python 代码
- 让 Claude 按对话方式编写和维护 CI 配置
- 用托管 runner 在云端执行与本地一致的构建

## 场景标签

 · 领域:开发工具/CI-CD

## 证据(README 行号)

> L11:  CI/CD as real code. Write your pipelines in Python, then run the exact same pipeline locally in Docker or on manag
> L44: - **Claude writes it for you** — `hm init` installs Claude Code skills that

## 星数曲线

```mermaid
xychart-beta
    title "harmont-dev/harmont-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2ffe95284e14` · [字段定义](../../DATASET.md)*
