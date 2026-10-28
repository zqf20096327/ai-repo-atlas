# sn0w12/ComfyUI-Sn0w-Scripts

⭐ 19 · Python · MIT · 推送 2026-06-27 · [GitHub](https://github.com/sn0w12/ComfyUI-Sn0w-Scripts) · 个人维护

**给 ComfyUI 用户的 LoRA 管理与杂项自定义节点集合**

面向 ComfyUI 用户的自定义节点扩展，核心功能围绕 LoRA 管理：自定义 LoRA 加载器（按文件夹路径配置、按标签相似度自动加载）、收藏置顶、按名称或修改时间排序；另含角色选择器、Prompt 合并与冗余标签简化、括号文本高亮、可自写调度器（附 Sigmoid 示例）、Lora Tester 批量出图、图像放大等节点。安装方式为克隆到 custom_nodes 目录或经 ComfyUI-Manager 安装；自定义加载器需在 extra_model_paths.yaml 中配置路径。

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

- 自定义 LoRA 加载器：按文件夹路径配置并按标签相似度自动加载（可设置最大差异、数量上限与排除文件夹）
- 收藏 LoRA 与角色置顶、按字母或修改时间排序
- Lora Tester 节点按 kohya_ss 命名格式自动批量生成测试图
- 可在 src/custom_schedulers 目录自写调度器，附 Sigmoid 示例

## 适用场景

- 管理大量按 SD1.5/XL/SD3 分类的 LoRA 文件
- 批量测试 LoRA 效果并对比出图
- 组合角色与提示词并自动清理冗余标签

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: This extension contains a collection of nodes and improvements created for lora management and general quality of li
> L16: 1. Install ComfyUi.

## 星数曲线

```mermaid
xychart-beta
    title "sn0w12/ComfyUI-Sn0w-Scripts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9cc53535a37b` · [字段定义](../../DATASET.md)*
