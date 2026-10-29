# NVIDIA/Broadcast-Skills

⭐ 19 · Standard ML · NOASSERTION · 推送 2026-10-02 · [GitHub](https://github.com/NVIDIA/Broadcast-Skills) · [官网](https://www.nvidia.com/broadcast-app/) · 组织维护

**让 AI Agent 通过 MCP 驱动 NVIDIA Broadcast 应用音视频 AI 特效**

NVIDIA 维护的 agent 技能包：通过 NVIDIA Broadcast 2.3+ 在本地回环地址暴露的 MCP 网关，让 AI agent 用自然语言开关和调节摄像头、麦克风、扬声器的 AI 特效，处理本地媒体文件（支持批量、暂停/恢复/重试），并列出与切换设备、更改摄像头分辨率帧率。要求 Windows + NVIDIA RTX GPU，agent 需支持 skills 并可作为 Streamable HTTP 的 MCP 客户端；不支持的客户端可走 stdio 桥接或配置文件注册。安装方式为克隆仓库并复制技能文件夹到 agent 的技能目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过本地 MCP 网关开关并调节摄像头/麦克风/扬声器 AI 特效
- 对本地媒体文件批量应用特效，支持暂停/恢复/取消/重试
- 设备列举切换与摄像头分辨率帧率调整
- 提供 stdio 桥接与配置文件两种 MCP 接入方式

## 适用场景

- 用对话让 AI agent 调节我的麦克风降噪和背景虚化
- 批量给本地视频文件应用降噪和 Studio Voice 处理
- 让 agent 列出摄像头并切换到指定分辨率帧率

## 场景标签

`图像视频处理` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agent skills that let an AI agent drive NVIDIA Broadcast — applying AI effects to your camera, microphone, and speak
> L57: - An **agent that supports skills and can act as an MCP client** over Streamable HTTP

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/Broadcast-Skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `acdd31927763` · [字段定义](../../DATASET.md)*
