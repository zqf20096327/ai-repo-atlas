# axhiao/QuickNote

⭐ 163 · Python · MIT · 推送 2026-02-02 · [GitHub](https://github.com/axhiao/QuickNote) · 个人维护 · 中文 README

**用视觉语言模型把截图转成 Markdown 笔记的 iOS/macOS 捕捉工具**

面向 iOS 与 macOS 用户的轻量捕捉工作流：用户截图后，QuickNote 将图像与提示词发送至视觉语言模型，转换为 Markdown 后保存到 Memos 进行长期检索与组织。设计上选择主动截图而非连续录屏，保留原图与提取文本。iOS 通过 Apple 快捷指令触发（可绑定 Action Button），macOS 通过 Raycast 热键触发。依赖独立部署的 Memos 作为笔记存储层，服务端用 docker compose 启动并配置 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 截图+提示词发送至 VL 模型，输出 Markdown 保存到 Memos
- 保留原图与提取文本，笔记带关键词与标签
- iOS 快捷指令触发（可绑 Action Button），macOS Raycast 热键触发
- 提供 docker compose 一键部署

## 适用场景

- 把随手截图转成可搜索的 Markdown 笔记
- 在 Memos 中长期组织和检索捕捉的内容
- 移动端与桌面端统一捕捉入口

## 场景标签

`知识库管理` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L9: Instead of continuously recording everything on your screen, QuickNote uses an intentional model: you only capture w
> L16: QuickNote was inspired by the discussion around Microsoft Recall, but follows the opposite design philosophy: selec

## 星数曲线

```mermaid
xychart-beta
    title "axhiao/QuickNote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-27 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e8327eb624f7` · [字段定义](../../DATASET.md)*
