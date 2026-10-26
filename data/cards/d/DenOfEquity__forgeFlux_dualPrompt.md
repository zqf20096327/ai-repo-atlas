# DenOfEquity/forgeFlux_dualPrompt

⭐ 39 · Python · 推送 2026-04-10 · [GitHub](https://github.com/DenOfEquity/forgeFlux_dualPrompt) · 个人维护

**Forge2 WebUI 扩展：为 Flux/SD3/SDXL 增加多提示词与采样控制**

Stable Diffusion Forge2 WebUI 的功能扩展：通过 SPLIT 关键字为 Flux、SD3、SDXL 等模型分别指定两个文本编码器的提示词；提供 Shift（base/max）参数控制、v-prediction 模型的 prediction type 覆盖、文本编码器单独禁用与设备选择、FluxTools（Canny/Depth/Redux/Fill）与 Flex.2、Flux LayerDiffuse 解码支持。安装经 WebUI Extensions 标签页从 URL 安装，部分功能需更新 diffusers 依赖或手动修改 Forge2 代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SPLIT 关键字实现双文本编码器分別提示（Flux/SD3/SDXL）
- Shift 参数控制与 HighRes fix 独立设置
- prediction type 覆盖（v-prediction 模型）
- FluxTools Canny/Depth/Redux/Fill 与 LayerDiffuse 透明 VAE 解码

## 适用场景

- 为 Flux 双编码器分别输入标签与自然语言提示词
- 使用 v-prediction 模型时覆盖预测类型
- 在 Forge2 中使用 FluxTools 的 Canny/Depth/Fill/Redux 控制

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: ## extra features extension for Forge2 webUI ##
> L19: Flux (CLIP-L / T5) assumed best usage is tags for first prompt, natural language for second.

## 星数曲线

```mermaid
xychart-beta
    title "DenOfEquity/forgeFlux_dualPrompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e2d0e94d3f3a` · [字段定义](../../DATASET.md)*
