# yoanbernabeu/NanoThumbnail

⭐ 52 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/yoanbernabeu/NanoThumbnail) · [官网](https://nanothumbnail.com) · 个人维护

**浏览器内生成/编辑/测试 YouTube 缩略图的 AI 工作室**

运行于浏览器的开源缩略图工作室，调用 Google Nano Banana 系列模型（Gemini 直连，OpenRouter 直连，Replicate 经 Netlify 代理），自带 API key，图像留在本地。功能含 brief 驱动生成（1-4 变体、多分辨率与画幅）、14 种风格、人物身份保持、蒙版局部编辑、对话式迭代、AI 点评、信息流预览与安全区测试；另提供 MCP 服务器让 Claude/Cursor 等 agent 驱动工作室。数据存 IndexedDB，可装为 PWA 离线使用，需 Node.js 22+ 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- brief 驱动生成：1-4 变体、1K/2K/4K、多画幅、14 种预设风格
- 蒙版局部编辑与对话式迭代，保留全部版本及谱系
- AI 点评（可读性/对比度/焦点等）与信息流预览、安全区、变体对比导出
- MCP 服务器让 Claude/Cursor 等 agent 驱动工作室，密钥与图像不离开浏览器

## 适用场景

- 给 YouTube 视频生成和迭代点击用缩略图
- 导入最多 14 张参考图或 YouTube 链接做同风格改编
- 在信息流预览中对比多个缩略图变体并导出用于 Test & Compare
- 让 AI agent 通过 MCP 代为执行生成、编辑与导出

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: NanoThumbnail is a free, open-source studio to **generate, edit and test YouTube thumbnails** with Google's Nano Ban
> L17: - **Brief-driven generation**: video title, scene, on-thumbnail text (rendered by the AI, or clean space left to ad

## 星数曲线

```mermaid
xychart-beta
    title "yoanbernabeu/NanoThumbnail 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `60679a63066e` · [字段定义](../../DATASET.md)*
