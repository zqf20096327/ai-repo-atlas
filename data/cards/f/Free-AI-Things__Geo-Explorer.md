# Free-AI-Things/Geo-Explorer

⭐ 30 · TypeScript · GPL-3.0 · 推送 2025-11-08 · [GitHub](https://github.com/Free-AI-Things/Geo-Explorer) · [官网](https://geo-explorer-orcin.vercel.app) · 个人维护

**AI 地理定位应用：上传照片或对话识别地点并规划行程**

基于 React/TypeScript 的对话式地理定位 Web 应用，通过 Gemini 模型实现：上传图片进行取证式分析（架构、植被、文字等线索）定位拍摄地点；自然语言查询地点与路线；生成多日行程。回答通过 googleSearch/googleMaps 工具实时接地并附来源。技术上采用双系统提示（图像/文本分离）、chain-of-thought 提示协议，以及用正则解析 AI 回复尾部指令驱动地图更新的 directive 机制。需自备 Gemini API key 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图片取证式地理定位（chain-of-thought 提示协议）
- 回答经 Google Search/Maps 实时接地并附来源
- 双系统指令按输入类型切换推理逻辑
- AI 回复尾部 directive 指令驱动地图/路线/建议更新

## 适用场景

- 上传照片识别拍摄地点并了解背景
- 对话式查询路线与周边地点
- 围绕某地生成多日旅行行程

## 场景标签

`聊天机器人` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L37: |**Forensic-Level Image Analysis**|Upload any photo, and the AI will perform a deep forensic analysis of architectu
> L70: - **What It Is:** The AI's ability to accurately identify locations from images by executing a complex, multi-step 

## 星数曲线

```mermaid
xychart-beta
    title "Free-AI-Things/Geo-Explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8417657bb7c3` · [字段定义](../../DATASET.md)*
