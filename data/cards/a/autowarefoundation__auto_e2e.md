# autowarefoundation/auto_e2e

⭐ 181 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/autowarefoundation/auto_e2e) · [官网](https://autoware.org) · 组织维护

**开源端到端自动驾驶模型：从环视相机直接生成车辆轨迹**

Autoware 基金会维护的相机优先端到端驾驶模型：将六个环视相机图像提升为鸟瞰图网格，由 GRU 规划器结合自车运动历史生成未来 6.4 秒的加速度与曲率轨迹，模型共 79.9M 参数、10 Hz 运行。当前发布的 Reactive 模型可直接使用，1 Hz 的 World Action 与 Reasoning 模型仍在开发中。提供 Hugging Face 检查点（nuPlan 与 KITScenes 训练）、KITScenes 验证集开环基准（ADE/FDE）与回放仪表盘；源码安装需 Python 3.12 与 PyTorch，支持 CPU 或 CUDA 构建。

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

- 六环视相机→鸟瞰图→GRU 规划器输出 6.4 秒轨迹（79.9M 参数，10 Hz）
- Hugging Face 提供检查点，支持零 shots 迁移到新城市与微调
- 在 KITScenes 验证集上与 7 个开源驾驶模型做开环 ADE/FDE 基准对比
- 只读 DataModelConsole 仪表盘回放相机场景与预测轨迹

## 适用场景

- 在 nuPlan/KITScenes 等数据集上做端到端轨迹预测研究与微调
- 为 Robotaxi 或 L2++ ADAS 原型提供相机端轨迹规划模型
- 复现并对比多个开源端到端驾驶模型的基准结果

## 场景标签

 · 领域:自动驾驶/机器人

## 证据(README 行号)

> L9:  An open-source, camera-first End-to-End driving model for highways, arterial roads and city streets.
> L21:  79.9 M parameters, 6 cameras, 6.4 s horizon, 10 Hz
> L27: AutoE2E is three cooperating models. The **Reactive model** runs at 10 Hz and drives: it lifts six surround cameras

## 星数曲线

```mermaid
xychart-beta
    title "autowarefoundation/auto_e2e 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 180 --> 182
    line [181, 181]
```

2026-10-18 181 → 2026-10-23 181（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `9305e179a724` · [字段定义](../../DATASET.md)*
