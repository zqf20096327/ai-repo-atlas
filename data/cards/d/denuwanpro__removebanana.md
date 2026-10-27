# denuwanpro/removebanana

⭐ 44 · JavaScript · MIT · 推送 2026-03-08 · [GitHub](https://github.com/denuwanpro/removebanana) · [官网](https://removebanana.eu.cc) · 个人维护

**npm 库：用逆 alpha 混合数学移除 Gemini 图像的 SynthID 水印**

面向 Node.js 开发者的图像处理 npm 包：针对 Google Gemini、Imagen 2/3、Nano Banana 生成图像中的不可见 SynthID 水印，通过模板相关检测水印位置（48×48 或 96×96）、提取 alpha 通道，再以 alpha 混合公式的数学逆运算重建原始像素，声称无损且不依赖 AI 猜测。提供文件路径与 Buffer 两种 API，可输出 png/jpeg/webp。运行需另装 node-canvas；另提供浏览器端在线工具 removebanana.eu.cc。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 alpha 混合公式逆运算重建原始像素（original = (watermarked − α×logo) / (1 − α)）
- 模板相关 + 粗到细匹配自适应检测水印位置
- 提供文件与 Buffer 两套 API，支持 png/jpeg/webp 输出
- 配套浏览器端在线工具，图像不上传

## 适用场景

- 批量处理 Gemini/Imagen 生成图像，移除 SynthID 不可见水印
- 在 Express 服务中集成水印移除接口
- 不想装环境时用浏览器在线工具处理单张图片

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Remove invisible AI watermarks from Google Gemini-generated images using reverse alpha blending mathematics.**
> L14: RemoveBanana uses the **exact mathematical inverse** of Google's alpha blending formula to perfectly reconstruct th

## 星数曲线

```mermaid
xychart-beta
    title "denuwanpro/removebanana 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-27 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6efe54346678` · [字段定义](../../DATASET.md)*
