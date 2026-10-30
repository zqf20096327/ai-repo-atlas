# NidAll/comfyui-ming-image-prompt-builder

⭐ 17 · JavaScript · GPL-3.0 · 推送 2026-09-26 · [GitHub](https://github.com/NidAll/comfyui-ming-image-prompt-builder) · 个人维护

**ComfyUI 节点：为 Ming 文生图工作流可视化构建结构化 JSON 提示词**

面向 ComfyUI 用户的自定义节点（节点 ID MingImagePromptBuilder）：在画布上拖拽矩形定义语义区域与层级，填写对象描述或精确文本，导出符合 Ming 提示词格式的 JSON 与布局预览、边界框输出。本体不含模型下载或推理，仅依赖 ComfyUI 已有依赖；JSON 通过 CLIP Text Encode 传入原生或官方 Ming 文本编码路径。提供导入校验、执行输入优先级、工作流持久化及 45 项后端测试与 Playwright 浏览器测试。已验证版本为 ComfyUI 0.37.0 / 前端 1.53.6。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化画布绘制语义区域并导出 Ming JSON 提示词
- 精确文本逐字保留并做一次性 JSON 转义，不被编辑器改写
- 输出 prompt/preview/bboxes/尺寸，bbox 采用嵌套逐帧约定
- 导入前完整校验文档，畸形输入抛出可操作错误而非静默置空

## 适用场景

- 在 ComfyUI 中为 Ming-Image Design 文生图搭建带区域布局的提示词
- 需要在生成图中出现精确指定文字的设计排版工作流
- 复用/导入既有 Ming JSON 提示词并继续可视化编辑

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: A visual structured-prompt editor for **Ming-Image-0.1-Design text-to-image** in ComfyUI. Draw rectangles for visibl
> L9: Place this repository at `ComfyUI/custom_nodes/ComfyUI-Ming-Image-Prompt-Builder/`, restart ComfyUI, and refresh the
> L11: The node ID is `MingImagePromptBuilder`. The frontend uses the standard ComfyUI `app`, `api`, and DOM-widget interf

## 星数曲线

```mermaid
xychart-beta
    title "NidAll/comfyui-ming-image-prompt-builder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e544cf4288dc` · [字段定义](../../DATASET.md)*
