# skkut/SilkStack-Image-Browser

⭐ 32 · TypeScript · MPL-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/skkut/SilkStack-Image-Browser) · [官网](https://skkut.github.io/silkstack) · 个人维护

**本地浏览与整理 ComfyUI 等 AI 生成图片的桌面浏览器**

基于 Electron/React 的本地图片浏览器，扫描文件夹并解析 ComfyUI、Automatic1111 等工具写入的元数据，支持按 prompt、模型、采样器等搜索过滤、自动监视输出目录、相似图堆叠、拖拽回 ComfyUI 加载工作流。它是 Image MetaHub v0.13.0 的 fork。语义搜索、AI 自动打标、相似度堆叠等 AI 功能属付费模块，经 WebGPU 在本地 GPU 运行，且该模块不包含在本仓库中，开源构建为纯图片浏览器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 ComfyUI/Automatic1111 元数据，按 prompt、模型、seed、CFG 等搜索过滤
- Auto-Watch 实时监视生成输出目录，可拖拽图片回 ComfyUI 加载工作流
- AI 功能（语义搜索、自动打标、相似度堆叠）付费且经 WebGPU 全本地运行，模块不在本仓库
- 开源构建不含 AI 模块，作为纯本地图片浏览器编译运行

## 适用场景

- 本地管理和检索 ComfyUI/A1111 生成的大量图片
- 生成过程中实时监视输出文件夹并按提示词找图
- 把相似生成结果堆叠分组并高亮 prompt 差异（付费功能）

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: **SilkStack Image Browser** is a **local image browser and manager** focused on viewing AI-generated images.
> L115: > **Note:** the `ai-intelligence` module (semantic search, auto-tagging, vector similarity) is *not* part of this 

## 星数曲线

```mermaid
xychart-beta
    title "skkut/SilkStack-Image-Browser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `145b273c57d6` · [字段定义](../../DATASET.md)*
