# matteodisalvo/HeroFig

⭐ 13 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/matteodisalvo/HeroFig) · 个人维护

**科研人员绘制论文出版级插图的桌面可视化编辑器**

基于 Electron/React 的科研图表桌面编辑器：从超过 1,000 个积木块和约 250 个成品图（Transformer、U-Net、NeRF 等模型图示）拖拽组装插图，按 CVPR/ICML/IEEE 等会议版式在真实打印尺寸下预览，检查小于 6pt 的文字与溢出，导出 PDF/SVG/PNG/TikZ 并可随保存自动写入论文文件夹（兼容 Overleaf）。支持局域网内实验室实时协作、灰度与色盲预览。AI 功能为可选：通过 Hugging Face 调用 FLUX.1-schnell 生成块配图，不启用则完全离线运行。提供 macOS（Apple silicon/Intel）与 Windows 安装包，也可用 Node.js 22+ 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,000+ 领域积木块与约 250 个知名模型成品图（Transformer、U-Net、NeRF、Llama 等）
- 按 CVPR/ICML/IEEE/NeurIPS/MICCAI 版式在打印尺寸下预览并检查文字大小与溢出
- 导出 PDF/SVG/PNG/TikZ，链接论文文件夹后每次保存自动更新
- 局域网内实验室实时协作与图上评论，无需云服务

## 适用场景

- 为论文快速绘制模型架构图等 hero figure
- 在投稿版式下核对插图尺寸与文字可读性
- 实验室多人协作编辑同一组论文插图并跟踪状态
- 直接导出 TikZ 到 LaTeX 工作流（含 Overleaf）

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L35: Pick a template or drag blocks from the library, write the labels, and HeroFig shows you the
> L59: - **Optional AI images**: illustrative pictures for your blocks, made by an open model through
> L112: Generating images is optional: HeroFig works fully without it. To make one you need a free

## 星数曲线

```mermaid
xychart-beta
    title "matteodisalvo/HeroFig 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `90751b2e9774` · [字段定义](../../DATASET.md)*
