# qwert2813434-ctrl/ALIGNED

⭐ 21 · TypeScript · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/qwert2813434-ctrl/ALIGNED) · [官网](https://aligned-app.github.io/en/) · 个人维护 · 中文 README

**Instagram 跨页轮播排版编辑器，AI 可直接生成其项目文件**

面向 Instagram 多页轮播设计的免费开源桌面排版编辑器（Mac/Windows，GPL-3.0），核心机制是整个轮播为一条连续画布、图片可跨页缝、导出时切分。支持拖曳吸附、参考线、群组对齐、九种滤镜、影片页导出 mp4、模板交换与字体导入。项目文件为文档化 JSON，附带 AI 规格说明与本机 MCP server（stdio，十项工具），供 Claude/GPT 等直接生成、读取与修改项目。限制：Windows 版不支持 .alignproj 单档打开与 mp4 导出；Mac 需 Apple Silicon + macOS 13+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 连续画布跨页对齐排版，导出时自动切分
- 项目文件为文档化 JSON，AI 读完规格即可生成可编辑项目
- 本机 MCP server（stdio、十项工具），不连模型 API、不上传项目
- Mac（公证 DMG）与 Windows（安装档）提供桌面构建

## 适用场景

- 在桌面大屏上排版并验收 Instagram 多页轮播
- 让 Claude/GPT 按 JSON 规格生成排版草稿，再在 App 中微调导出
- 通过 MCP 让 AI 直接读取并修改正在编辑的画布

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L44: ALIGNED 的專案檔是文件化的 JSON——**任何 AI 讀完規格就能直接產生「打開即可編輯」的專案**：
> L50: repo 內附本機 MCP server，讓支援 MCP 的 AI 不必手寫 JSON，就能讀取、驗證、建立與修改
> L3: **English:** ALIGNED is a free, open-source layout editor for multi-page Instagram carousels — the whole carousel is

## 星数曲线

```mermaid
xychart-beta
    title "qwert2813434-ctrl/ALIGNED 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `02e84564922e` · [字段定义](../../DATASET.md)*
