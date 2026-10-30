# ThepExcel/ComfyAngel

⭐ 16 · Python · 推送 2026-08-15 · [GitHub](https://github.com/ThepExcel/ComfyAngel) · [官网](https://registry.comfy.org/publishers/thepexcel/nodes/comfyangel) · 个人维护

**ComfyUI 自定义节点集：文本排列、循环、参数叠加与可视化编辑**

面向 ComfyUI 用户的自定义节点集合，共 18 个节点，覆盖四类功能：Text Permutation 用 {a,b} 语法生成提示词组合、Loop Start/End 在不依赖 Auto Queue 的情况下实现单次执行内的循环与结果累积、Parameter Overlay 将生成参数以可视化形式叠加到图片上、Smart Composite/Smart Crop 提供拖拽定位与裁剪的可视化编辑器。另含批量图片加载、JSON 字段提取、取色器等工具节点。支持 A1111/Civitai 与 ComfyUI 格式的生成元数据读取。安装途径为 ComfyUI Registry、ComfyUI Manager 或手动 git clone。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- {cat,dog} 语法生成全部提示词组合用于批量生成
- 无需 Auto Queue 的循环节点，图像张量拼接、字符串收集
- Smart Composite 提供拖拽定位、9 种混合模式与蒙版透明度
- 解析 A1111/Civitai 与 ComfyUI 嵌入的生成元数据并叠加显示

## 适用场景

- 批量生成多组提示词组合的图片
- 给生成结果叠加参数信息便于分享对比
- 可视化地合成水印或叠加图层

## 场景标签

`图像生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L1: # ComfyAngel
> L3: Custom nodes for ComfyUI that make batch workflows easy and visual editing intuitive.

## 星数曲线

```mermaid
xychart-beta
    title "ThepExcel/ComfyAngel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `270538fca205` · [字段定义](../../DATASET.md)*
