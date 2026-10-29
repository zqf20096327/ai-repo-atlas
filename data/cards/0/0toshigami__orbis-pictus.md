# 0toshigami/orbis-pictus

⭐ 28 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/0toshigami/orbis-pictus) · 个人维护

**点击即探索的 AI 绘制图画书浏览器，每页实时生成**

一个自托管 Web 应用：用户输入任意查询，应用通过 LLM 撰写页面内容提示词、文生图模型实时绘制整页图像；点击图中任意物体，视觉模型识别点击对象并生成关于该对象的新页面，无 HTML 标记与链接。支持搜索、编辑命令、页面版本分支、面包屑导航、三种缓存层去重，以及实验性的闲置循环视频与页面过渡变形（默认关闭）。内容与视觉风格提示词分离，风格可整体切换。需 Node 22.5+ 与至少一个真实 LLM 凭据运行，是对 flipbook.page 的独立致敬项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 点击坐标标记 + 视觉模型识别点击对象，生成子页面
- 内容与风格提示词分离，5 种风格与 4 种构图可即时切换
- 三层缓存：坐标网格 VLM 缓存、主题级子页去重、提示词哈希图像缓存
- 页面版本为一等公民，分支控制可切换与加星默认版本

## 适用场景

- 以生成图像方式无限探索任意主题
- 输入编辑命令（如‘改成夜晚’）生成同一页面的新版本
- 自托管一个可定制的 AI 图画书式浏览体验

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: You type anything, and the app draws a page in real time. You click anything inside that image, and
> L50: |Prompt authoring + tap vision (LLM)|Anthropic (or any Anthropic-compatible proxy) · Google Gemini|
> L51: |Image generation|fal.ai · BytePlus Ark (Seedream) · Google Gemini ("nano banana") · OpenAI (gpt-image)|

## 星数曲线

```mermaid
xychart-beta
    title "0toshigami/orbis-pictus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d55a9e841b15` · [字段定义](../../DATASET.md)*
