# incredible404-rgb/Colab-yoga

⭐ 38 · Python · Apache-2.0 · 推送 2026-11-14 · [GitHub](https://github.com/incredible404-rgb/Colab-yoga) · 个人维护 · 中文 README

**系统托盘的 Colab GPU 管理台：唤醒/释放大模型实例并自动关停**

常驻 Windows/macOS 系统托盘的原生管理台（Go + MyGo 界面），管理 Google Colab 付费 GPU 上的大模型实例：一键唤醒、加载与切换模型、续时、释放，显示余额、计费速率、显存与各入口连通状态，独立 keeper 进程保活，闲置默认 30 分钟自动关停。模型本身由 colab-gpu-llm-service 仓库提供，通过 Tailscale 暴露 llama-server :8081 供网页对话、Magpie 和本机 MCP 使用；对话流量不经过本工具。提供免安装包与源码安装两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 唤醒/释放 Colab GPU 实例，独立 keeper 保活，闲置 30 分钟自动关停
- 余额、计费速率、显存、推理槽位与网页/API/Magpie/MCP 连通状态展示
- 本机 MCP 桥自动启动与恢复，最后会话结束安全关闭
- 附带给 Claude Code、Codex 等 agent 的技能文件（花钱动作先确认）

## 适用场景

- 租用 Colab 付费 GPU 跑自己的大模型并随时开关，控制花费
- 让闲置的 Colab 实例自动释放，避免忘记关机持续计费
- 通过 Tailscale 在网页对话、Magpie、本机 MCP 中使用同一模型服务

## 场景标签

 · 领域:LLM 基础设施/GPU 资源管理

## 证据(README 行号)

> L7: 常驻系统托盘的 Colab GPU 管理台：一键唤醒、释放 Google Colab 付费 GPU 上的大模型实例，随时查看余额和各入口是否连通，没人用时自动关停。
> L9: 在 Google Colab 付费 GPU（默认 G4 · RTX PRO 6000 96 GB）上跑自己的大模型，并通过 Tailscale 把 llama-server :8081 提供给网页对话、Magpie 和本机 MCP 
> L17: 模型本身（colab_kernel 启动脚本、模型清单、中文思考补丁、本机 MCP 服务）在 colab-gpu-llm-service 项目里，不在这个仓库。管理台的模型列表就是导出的 `colab_kernel_runners

## 星数曲线

```mermaid
xychart-beta
    title "incredible404-rgb/Colab-yoga 星数(近 7 点)"
    x-axis ["2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19"]
    y-axis "stars" 11 --> 40
    line [13, 30, 31, 32, 35, 37, 38]
```

2026-11-12 13 → 2026-11-19 38（+25）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `568b7ea5bf30` · [字段定义](../../DATASET.md)*
