# etaisella/Prox-E

⭐ 19 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/etaisella/Prox-E) · [官网](https://etaisella.github.io/Prox-E/) · 组织维护

**SIGGRAPH'26 论文官方实现：基于基元抽象的细粒度 3D 形状编辑框架**

Prox-E 的官方 PyTorch 实现，训练无关的 3D 编辑框架：将输入 3D 形状抽象为几何基元集合，由预训练视觉语言模型（默认 Gemini，可选 GPT 或本地 Qwen）编辑该抽象以指定基元级修改，再用 TRELLIS 3D 生成模型引导局部修改并保持未变区域。需 Python 3.11 conda 环境、TRELLIS 模型权重、Blender 与 SuperDec 检查点。面向 3D 视觉与图形学研究人员，附评测代码与 ShapeTalk 基准数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入 3D 形状抽象为几何基元，VLM 编辑抽象后引导 3D 生成模型做局部修改
- VLM 后端可选 Gemini/GPT/本地 Qwen（本地模式无需 API key）
- 统一评测器输出 7 项指标（身份保持/3D 质量/编辑保真度）
- 提供 ShapeNet/Edit3D-Bench/Toys4K 演示与自定义 mesh 推理命令

## 适用场景

- 对自定义 3D 模型按自然语言指令做局部结构编辑
- 复现论文实验并评测 3D 编辑结果
- 比较不同 VLM 后端在代理编辑阶段的表现

## 场景标签

 · 领域:3D 视觉/图形学

## 证据(README 行号)

> L30: Text-based 2D image editing models have recently reached an impressive level of maturity, motivating a growing body
> L86: By default, Prox-E uses Gemini as the VLM backbone in the proxy editing and prompt parsing stages. Set your Google 

## 星数曲线

```mermaid
xychart-beta
    title "etaisella/Prox-E 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f90dee027aef` · [字段定义](../../DATASET.md)*
