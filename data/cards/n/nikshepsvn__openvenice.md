# nikshepsvn/openvenice

⭐ 65 · TypeScript · 推送 2026-04-17 · [GitHub](https://github.com/nikshepsvn/openvenice) · 个人维护

**Venice AI 的自托管多模态前端：聊天/图像/音频/视频/工作流**

面向 Venice AI API 的开源 Web 前端，纯静态站点、无后端：API key 存于浏览器直连 Venice 接口。功能覆盖流式聊天（含附件/引用/联网搜索）、图像生成与编辑放大、50+ 语音的 TTS 与 Whisper 转录、音乐与视频生成、文本嵌入，以及节点式可视化工作流和用自然语言搭建工作流的 Playground。支持自托管分享给家人共用一个 key。技术栈为 React 19/TypeScript/Vite，提供 npm 构建、静态托管、多阶段 Dockerfile 与 Railway 一键部署三种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天/图像/音频/音乐/视频/嵌入六类模态统一界面
- 可视化节点工作流，含相册封面、播客、音乐视频等启动模板
- 无后端：API key 留在浏览器，可 AES-GCM 加密后存 localStorage
- Playground 对话式生成与编辑工作流

## 适用场景

- 不想用官方界面、想自托管并自定义 AI 界面
- 与家人共享一个 Venice API key 提供干净的 AI 入口
- 用可视化工作流串联多模型产出图像/音乐/视频

## 场景标签

`聊天机器人` `图像生成` `语音合成` `视频生成` · 领域:对话与助手

## 证据(README 行号)

> L3: A customizable, open-source frontend for the Venice AI API.
> L21: ### Chat
> L39: ### Workflows

## 星数曲线

```mermaid
xychart-beta
    title "nikshepsvn/openvenice 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-31 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `72a7d4215627` · [字段定义](../../DATASET.md)*
