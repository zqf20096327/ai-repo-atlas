# PRITHIVSAKTHIUR/FLUX.2-Klein-LoRA-Studio

⭐ 22 · HTML · Apache-2.0 · 推送 2026-08-12 · [GitHub](https://github.com/PRITHIVSAKTHIUR/FLUX.2-Klein-LoRA-Studio) · [官网](https://huggingface.co/spaces/prithivMLmods/FLUX.2-Klein-LoRA-Studio) · 个人维护

**基于 FLUX.2-klein-9B 的图生图编辑与风格迁移工作台**

构建在 black-forest-labs/FLUX.2-klein-9B 模型之上的实验性图生图编辑与风格迁移平台，整合多个专用 LoRA 适配器：Klein-Consistency（一致性保持）、Klein-Delight-Style（光照中性化）、Best-Face-Swap（身份保持换脸）、Ghost-Mannequin（3D 服装体积）。以 FastAPI 后端与深色单页 Web 界面提供，含 A/B 对比滑块、历史胶片条、快速提示词。需 CUDA GPU，通过 uv 或 pip 安装依赖本地运行，另有 Hugging Face 在线演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多个专用 LoRA 适配器按需懒加载与权重融合
- 双输入身份保持换脸（背景环境+目标面部）
- 4 步采样窗口内的文本引导图像编辑
- SPA 界面：A/B 对比滑块、历史记录、编辑链式叠加

## 适用场景

- 对商品图做一致性保持的风格与视角变换
- 结合底图环境与指定人像做换脸编辑
- 服装电商图生成 3D 人体体积效果
- 在浏览器中对比编辑前后效果并链式多次编辑

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: FLUX.2-Klein-LoRA-Studio is an experimental, high-performance image-to-image manipulation and style-transfer platfor
> L13: * **Text-Guided Image Editing:** Enables style transformations, camera angle shifts, lighting neutralization, and a

## 星数曲线

```mermaid
xychart-beta
    title "PRITHIVSAKTHIUR/FLUX.2-Klein-LoRA-Studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a61955edfbf6` · [字段定义](../../DATASET.md)*
