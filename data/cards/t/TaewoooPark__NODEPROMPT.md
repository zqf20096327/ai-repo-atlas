# TaewoooPark/NODEPROMPT

⭐ 44 · TypeScript · MIT · 推送 2026-04-27 · [GitHub](https://github.com/TaewoooPark/NODEPROMPT) · 个人维护 · 中文 README

**将提示词分解为 3D 概念图并重新合成结构化提示的交互工具**

NodePrompt 把文本、图片或 PDF 提示词分解为多维概念图，在 3D 球面（斐波那契晶格）、2D 同心环与双曲内部视图三种模式下渲染，用户可拖拽节点、调节权重、连边编辑后由 AI 重新合成为结构化提示词。节点按六个先验维度分类，支持 MediaPipe 摄像头手势控制，可接入六家 LLM 提供商（统一接口，需 API key）。以 Node.js 18+ / Vite 源码方式本地运行，浏览器中配置密钥（仅存 localStorage），生产部署需自建后端代理。

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

- 文本/图片/PDF 分解为可空间编辑的概念图，再合成结构化提示词
- Sphere/Radial/Interior 三种交互模式，GSAP 平滑过渡
- 六个先验维度（ens/res/unum/aliquid/verum/bonum）节点类型体系
- MediaPipe 手势控制与多模态附件（图片 5MB / PDF 10MB）支持

## 适用场景

- 把模糊的想法或论文 PDF 分解为可编辑的概念结构再生成提示词
- 在 3D 空间中可视化管理复杂提示词的结构与权重
- 比较不同 LLM 提供商对同一提示词的概念分解结果

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L22: NodePrompt decomposes prompts — text, images, or PDFs — into multi-dimensional concept graphs, renders them on a 3D
> L43: The core innovation is **Human-AI Co-Decomposition**: AI proposes a conceptual structure, humans reshape it spatial

## 星数曲线

```mermaid
xychart-beta
    title "TaewoooPark/NODEPROMPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f114c1ed184f` · [字段定义](../../DATASET.md)*
