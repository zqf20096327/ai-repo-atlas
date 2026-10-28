# acorderob/sd-webui-prompt-postprocessor

⭐ 55 · Python · MIT · 推送 2026-08-14 · [GitHub](https://github.com/acorderob/sd-webui-prompt-postprocessor) · 个人维护

**SD WebUI/ComfyUI 的提示词后处理扩展：通配符、变量、负迁移等**

面向 Stable Diffusion 生态用户的提示词后处理扩展（原 sd-webui-sendtonegative），兼容 ComfyUI、Forge、Forge Neo/Classic、reForge、SD.Next、AUTOMATIC1111 WebUI 等。功能包括：处理通配符（兼容 Dynamic Prompts 格式）、将提示词部分内容发送到负向提示词、定义模型变体并检测当前模型、用户变量与条件内容、按条件映射 LoRA 等 extranetwork（虚拟 LoRA）、清理多余分隔符与空格、组合模式。安装通过 WebUI 扩展页面或 ComfyUI Custom Nodes Manager 以 Git URL 方式完成；限制包括需在其他修改提示词的扩展之后加载、不识别 TE2/TE3 分词器分隔符等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将正向提示词中的内容发送到负向提示词（扩展原始功能）
- 模型变体检测与条件化 LoRA 映射（虚拟 LoRA）
- 处理 __wildcard__ 与 {choice|choice} 格式通配符，兼容 Dynamic Prompts
- 清理提示词中多余分隔符与空格

## 适用场景

- 在通配符生成流程中动态向负向提示词注入内容
- 切换不同底模（pony/illustrious 等）时自动映射对应的 LoRA
- 整理和清理冗长提示词中的冗余符号

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: The Prompt PostProcessor (or PPP, formerly known as "sd-webui-sendtonegative"), is an extension designed to process 
> L11: * AUTOMATIC1111 Stable Diffusion WebUI

## 星数曲线

```mermaid
xychart-beta
    title "acorderob/sd-webui-prompt-postprocessor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `da687d5c2df0` · [字段定义](../../DATASET.md)*
