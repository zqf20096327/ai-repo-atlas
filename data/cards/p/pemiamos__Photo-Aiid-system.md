# pemiamos/Photo-Aiid-system

⭐ 15 · Python · 推送 2026-06-30 · [GitHub](https://github.com/pemiamos/Photo-Aiid-system) · 组织维护 · 中文 README

**桌面 AI 照片管理与多人网页征稿协作系统**

面向摄影爱好者与画册组稿团队的双模式应用：桌面端在本机扫描照片，AI 自动分类打标、提取摄影师与拍摄地点、离线反向地理编码到中文市县级，并通过历史索引跨全库检索；v3.0 起增加网页征稿链路——摄影师凭投稿码浏览器直传阿里云 OSS，编辑用桌面 App 远程建书、发码、看板管理与选片，OSS 主存并每 15 分钟增量镜像到 Cloudflare R2。AI 引擎可选 Ollama/CLIP 本地或智谱 GLM/Claude/Gemini 云端；源码运行需 Node 18+ 与 Python 3.10+，另提供 Mac/Windows 打包版（Tauri 封装）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 历史索引跨全库按摄影师/地点/标签/类别/文件名秒搜
- 多引擎 AI 识别：Ollama/CLIP 本地或智谱 GLM/Claude/Gemini 云端
- 内置 3238 条行政区划的离线反向地理编码
- 投稿码网页征稿 + STS 临时凭证浏览器直传 OSS + R2 增量备份

## 适用场景

- 本地整理海量照片：AI 打标、批量重命名、跨全库关键词检索
- 画册/选题组稿：向多位摄影师发放投稿码网页征稿并统一管理
- 需要隐私优先的本地 AI 引擎（Ollama/CLIP）处理照片

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L10: 桌面端在本机就地整理照片（AI 识别 / 批量重命名 / 语义搜索），**v3.0 起**扩展出一整套
> L41: - 🤖 **AI 自动识别** — 智能分类、打标、提取摄影师与拍摄地点，强 JSON 模式 + 安全校验
> L42: - 🔀 **多引擎切换** — 本地 Ollama / CLIP（隐私优先）或云端 **智谱 GLM（glm-4v-flash 免费）** / Claude / Gemini

## 星数曲线

```mermaid
xychart-beta
    title "pemiamos/Photo-Aiid-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8b0d712c0d05` · [字段定义](../../DATASET.md)*
