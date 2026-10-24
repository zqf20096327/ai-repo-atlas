# WP-Autoplugin/wp-autoplugin

⭐ 397 · PHP · 推送 2026-10-11 · [GitHub](https://github.com/WP-Autoplugin/wp-autoplugin) · [官网](https://wp-autoplugin.com) · 组织维护

**在 WordPress 后台用 AI 代理创建、修改与审查插件的工具**

WordPress 管理后台内的代理式编码工作流：通过 Plan → Code → Review 三个阶段，从描述生成完整插件、修复或扩展现有插件/主题、以钩子方式做扩展插件，并用持久对话解释陌生代码库。代理以有界的只读源码工具渐进探索项目，生成精确的有界搜索替换操作，产物以不可变修订形式暂存，未经管理员批准不改动线上文件。自带 API key 模式，可连接 OpenAI、Anthropic、Google Gemini、xAI 或兼容端点，也可用 ChatGPT 订阅的 Codex 额度。要求 WordPress 6.6+ 与 PHP 8.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Plan → Code → Review 三阶段工作流，计划与修订均为不可变版本
- 代理用有界只读源码工具渐进探索代码库，而非整库塞入提示词
- 生成结果暂存且原子化，需管理员显式批准才发布到线上
- 支持图像输入（JPEG/PNG/WebP）配合视觉模型做界面复刻与错误解释

## 适用场景

- 用一句描述在后台直接生成完整 WordPress 插件
- 修复或给已安装插件/主题加功能而不立即改动原文件
- 通过持久对话理解不熟悉的插件代码结构
- 用截图或 mockup 让 AI 复刻界面或修布局问题

## 场景标签

`编码 Agent` `代码生成` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: WP-Autoplugin brings an agentic coding workflow into WordPress. From the WordPress admin, it can explore an existing
> L5: It is completely free and bring-your-own-key: you can connect it directly to OpenAI, Anthropic, Google Gemini, xAI, 

## 星数曲线

```mermaid
xychart-beta
    title "WP-Autoplugin/wp-autoplugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 396 --> 398
    line [397, 397]
```

2026-10-18 397 → 2026-10-24 397（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `de4b8b40c92f` · [字段定义](../../DATASET.md)*
