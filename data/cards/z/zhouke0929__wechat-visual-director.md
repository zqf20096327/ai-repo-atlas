# zhouke0929/wechat-visual-director

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/zhouke0929/wechat-visual-director) · [官网](https://zhouke0929.github.io/wechat-visual-director/) · 个人维护 · 中文 README

**微信公众号 AI 排版 Skill：Agent 把选题或 Markdown 做成可发布的推文**

面向公众号运营与内容创作者的开源 AI 排版 Skill 加本地可视化工作台：Agent 接收选题、资料或 Markdown，完成语义规划与版式设计，通过受控组件转换为微信兼容 HTML；用户在本地工作台编辑正文、审核 AI 配图、切换 12 套主题并以手机预览校对，最终复制富文本或经微信 API 创建草稿。支持基于组件参考图创作自定义主题并导出 .vdtheme 扩展包。安装依赖能执行本机命令的 Agent 宿主（Codex/OpenCode），项目处于 Alpha 阶段，暂无 Linux 便携安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 12 套内置主题，切换主题保留正文与已有图片，不重新调用图片模型
- 12 类语义组件 + 14 种基础样式，受控组件完成 Markdown 到微信兼容 HTML 转换
- 本地工作台支持原文编辑、AI 配图审核、桌面校对与手机预览
- 可配置微信 API 交付草稿，也可不接 API 直接复制富文本

## 适用场景

- 把已写好的 Markdown 稿件排版成公众号推文
- 给 Agent 一张组件参考图，创作整套自定义主题并复用
- 从选题和资料出发，让 Agent 规划结构并生成配图候选
- 在工作台里改文字、审图片并手机预览后交付草稿

## 场景标签

`图像生成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: **WeChat Visual Director（公众号视觉主编）是一套开源的微信公众号 AI 排版 Skill + 本地可视化工作台。** Agent 理解内容、设计版式，你在工作台改文字、审图片、看手机效果，最后复制图文或交付
> L21: 适合公众号运营、新媒体团队和内容创作者。首次体验无需配置微信 API 或额外的项目图片 Key；先完成排版，再按需配图和交付。Agent 本身仍需可用的模型与额度。
> L110: 1. **在 Agent 对话里开始。** 给一个选题、一组资料，或粘贴现成的纯文本 / Markdown。Agent 整理结构、完成语义规划，再返回本地任务链接。

## 星数曲线

```mermaid
xychart-beta
    title "zhouke0929/wechat-visual-director 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `94ce9c28f8e0` · [字段定义](../../DATASET.md)*
