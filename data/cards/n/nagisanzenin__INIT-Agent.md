# nagisanzenin/INIT-Agent

⭐ 20 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/nagisanzenin/INIT-Agent) · [官网](https://initlabs.si) · 个人维护

**可改写自身 harness 的自修改编码 agent（研究预览版）**

Rust 编写的编码 agent，允许模型在任务中修改自己的 harness——提示词、工具、循环与编译核心。固定部分为 Root：独立进程持有密钥、签名日志与快照，通过 G0–G4 门控、沙箱（Seatbelt/bubblewrap）与回滚机制检查每次自修改。编译核心热切换需完整构建（冷构建约 13 分钟）。默认完全访问文件与网络，workspace 模式限制写入范围。定位研究预览，仅 macOS 14+ Apple silicon 与实验性 Linux x86_64，Windows 未支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 可修改自身 harness，含编译的 Rust 核心（热切换为新进程）
- Root 独立进程：门控（G0–G4）、沙箱、签名记录、回滚（/rollback、/panic）
- 密钥只存于 Root，不进入 agent；花费计量不设上限
- 默认完全访问模式，另有 workspace 限制模式

## 适用场景

- 研究自修改 agent 的行为与安全边界
- 让编码 agent 随模型能力增长调整自身 harness
- 观察自修改的门控、密封测试与回滚机制

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: INIT is a coding agent that rewrites its own harness while it works. The harness is everything around the model: pro
> L55: INIT 0.5 is a research preview.
> L57: - **Tested:** DeepSeek (deepseek-flash, deepseek-v4-pro) on the live API. At $0 on a mock model, the v0.5.2 bundles

## 星数曲线

```mermaid
xychart-beta
    title "nagisanzenin/INIT-Agent 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-29 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `337867dc64ab` · [字段定义](../../DATASET.md)*
