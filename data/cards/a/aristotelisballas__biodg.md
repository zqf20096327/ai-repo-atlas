# aristotelisballas/biodg

⭐ 27 · Python · Apache-2.0 · 推送 2025-12-12 · [GitHub](https://github.com/aristotelisballas/biodg) · 个人维护

**面向心电/脑电分类的域泛化算法评测基准套件**

基于 PyTorch 的域泛化（Domain Generalization）评测套件，基于 DomainBed 改造用于一维生物信号分类：收录 ERM、IRM、MMD、CORAL、RSC 五种算法，ECG 数据来自 2020 PhysioNet Challenge 四个数据库，EEG 数据来自上海交大 BCMI 实验室的 SEED 系列数据集（需申请获取）。工作流程包括下载数据、转换为 PyTorch DataLoader 格式、配置 bioconfig.py 路径后以命令行脚本训练。配套论文发表于 IEEE TETCI，代码以 MIT 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 5 种域泛化算法（ERM/IRM/MMD/CORAL/RSC）
- ECG（PhysioNet 2020）与 EEG（SEED 系列）双基准数据集
- 提供数据转换、配置与训练的完整命令行流程
- 配套论文发表于 IEEE TETCI，MIT 许可

## 适用场景

- 在标准基准上评测域泛化算法在 ECG/EEG 分类上的表现
- 复现论文中的域泛化实验结果
- 研究跨数据库/跨中心的生物信号分类泛化性

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: BioDG is a PyTorch suite containing benchmark datasets and algorithms for domain generalization,
> L6: The available algorithms were based on DomainBed and modified

## 星数曲线

```mermaid
xychart-beta
    title "aristotelisballas/biodg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9bf85f9db011` · [字段定义](../../DATASET.md)*
