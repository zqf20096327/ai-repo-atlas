# mattn/go-jev

⭐ 46 · Go · MIT · 推送 2026-09-23 · [GitHub](https://github.com/mattn/go-jev) · 个人维护

**面向 TypeSafe Jev 决策模型的 Go SDK 与 CLI 工具**

为 TypeSafe Jev 决策专用模型提供 Go SDK 与 jev-cli 命令行工具。模型返回类型化答案（yes/no 概率、选项、加权分）而非文本；SDK 通过 WithAPIKey/WithModel/WithURL 等选项构造客户端，支持批量 Evaluate、429/529 指数退避重试，可指向本地 tensai 服务器（同一 API）。CLI 提供 noul/choice/score/grep/ask 命令，可接收 stdin 管道、JSON 状态与并发处理，适配 UNIX 管道场景。发布页提供 Linux/macOS/Windows 预编译二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种类型化输出：noul 概率、choice 选项、score 加权分
- jev-cli 支持 stdin 管道、逐行并发处理与 grep 式过滤
- 429/529 自动指数退避重试（默认 3 次）
- 可切换端点至本地 tensai 服务器

## 适用场景

- 在 Go 程序中调用 Jev 模型获得结构化的决策结果
- 在 shell 管道中批量判定文本（如过滤紧急工单）
- 本地部署 tensai 服务器后离线使用同一 API

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L3: Go SDK for TypeSafe Jev, a decision-only model
> L51: go install github.com/mattn/go-jev/cmd/jev-cli@latest

## 星数曲线

```mermaid
xychart-beta
    title "mattn/go-jev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2578f1f1c067` · [字段定义](../../DATASET.md)*
