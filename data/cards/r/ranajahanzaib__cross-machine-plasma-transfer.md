# ranajahanzaib/cross-machine-plasma-transfer

⭐ 3 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ranajahanzaib/cross-machine-plasma-transfer) · 个人维护

**面向聚变研究者的托卡马克迁移学习分析工作台**

开源科研工作台，研究磁平衡重构在 DIII-D 与 MAST 两台托卡马克间的域偏移与迁移学习问题：提供 ProtocolGuard 防标签泄漏的三协议流程、物理线圈几何引擎、Wasserstein/KS/MMD 统计域偏移诊断、CORAL 与最优传输无监督域自适应基准、65×65 极向磁通面重构及 k-NN OOD 风险检测。前端为 Next.js 14 仪表盘（D3.js/Canvas），后端 FastAPI 分析服务，附带 plasma-transfer CLI 与 pytest 测试套件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ProtocolGuard 强制执行 A/B/C 三种实验协议并防止目标标签泄漏
- 统计域偏移诊断：Wasserstein、KS、MMD 与 shot 分层域分类器
- CORAL 协同对齐与 Sinkhorn 最优传输的无监督域自适应基准
- FastAPI 后端 + Next.js 14 仪表盘，附带 plasma-transfer CLI 与 16 项测试

## 适用场景

- 分析模型在两台托卡马克间迁移失败的物理成因
- 在无目标标签条件下做零样本磁通重构实验
- 可视化托卡马克运行状态的共享特征流形与域间分布差异

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: An open-source scientific research workbench for investigating domain shift, transfer learning, uncertainty, and cro
> L16: - **2D Poloidal Flux Reconstruction ($\psi(R, Z)$):** Reconstructs $65 \times 65$ magnetic flux surfaces, edge safe


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0e18782d3c9b` · [字段定义](../../DATASET.md)*
