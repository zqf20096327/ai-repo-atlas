# safdev758/agentpackettracer

⭐ 13 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/safdev758/agentpackettracer) · 个人维护

**嵌入 Cisco Packet Tracer 的 AI 助手：规划与配置网络实验**

在 Cisco Packet Tracer 内运行的 AI 代理，由本地 Python 后端驱动：检查实验拓扑、规划变更、创建设备、连接线缆、配置主机与 CLI，并核验实际 CLI 结果，不修改 Cisco 可执行文件。支持 OpenAI、Google Gemini、OpenRouter（自带 API key），可选通过 @codex 调用本地 Codex CLI 无头 worker。会话记忆有界并在超限时压缩为事实上下文，工具验证强制执行模式，禁止将 CLI 错误或未完成 ping 报告为成功。当前为实验性 Linux 发行版，测试于 Packet Tracer 9.0.0.0810，Windows 计划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 代理可在模拟器内创建设备、连线、配置 CLI 并核验实际结果
- 多提供商可选（OpenAI/Gemini/OpenRouter），使用用户自有 API key
- 可选 @codex 本地无头 worker，使用用户自身 Codex CLI 与登录
- 有界会话记忆跨追问保留需求与工具观察，超限压缩为事实上下文

## 适用场景

- 让 AI 代为搭建和配置 Packet Tracer 网络实验
- 通过对话获取网络解释与变更规划
- 实验中诊断设备状态并验证配置是否生效

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: An AI assistant inside Cisco Packet Tracer, backed by a local Python service. Inspect a lab, plan changes, configure
> L30: - **Inspect:** read device state, recover harmless CLI prompts and run diagnostics.
> L33: Choose OpenAI, Google Gemini or OpenRouter in Settings and use your own API key. Model discovery does not prove end

## 星数曲线

```mermaid
xychart-beta
    title "safdev758/agentpackettracer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `70a1facf5627` · [字段定义](../../DATASET.md)*
