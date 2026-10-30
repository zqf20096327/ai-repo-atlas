# shootthesound/lora-the-explorer

⭐ 59 · Python · MIT · 推送 2025-11-05 · [GitHub](https://github.com/shootthesound/lora-the-explorer) · 个人维护

**带 GUI 的 FLUX LoRA 编辑工具：差分、合并、层级操控**

面向 FLUX LoRA 文件的操作工具，提供 Python GUI（lora_algebra_gui.py）：LoRA 差分去除冲突、传统加权合并、跨 LoRA 指定层合并、层级静音（如面部层 7/12/16/20）、元数据查看与直接编辑；自动检测并修复跨训练工具（AI-Toolkit/FluxGym/sd-scripts）的兼容性问题。核心处理依赖 kohya-ss 的 sd-scripts（sd3 分支），安装脚本自动搭建 venv 并下载依赖。支持 safetensors/ckpt/pt 格式，MetaEditor 为原地修改、无安全回退。

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

- LoRA 差分运算与层级定向静音（面部层 7/12/16/20）
- 跨 LoRA 指定层合并（面部A+风格B、补集拆分等预设）
- 兼容 AI-Toolkit/FluxGym/sd-scripts/kohya-ss 训练产物并自动修复元数据问题
- 安装脚本自动创建 venv 并下载 sd-scripts（sd3 分支）

## 适用场景

- 清理风格 LoRA 中混入的面部改动
- 把角色 LoRA 的面部层与风格 LoRA 合并生成混合作品
- 修复跨训练工具产生的不兼容 LoRA 文件

## 场景标签

 · 领域:生成式AI/模型资产工具

## 证据(README 行号)

> L7: This tool provides various FLUX LoRA manipulation techniques including difference operations, merging, targeted laye
> L210: LoRA the Explorer relies on sd-scripts by kohya-ss for the core LoRA processing functionality. Our installer autom

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/lora-the-explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-30 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `56e7cc22b942` · [字段定义](../../DATASET.md)*
