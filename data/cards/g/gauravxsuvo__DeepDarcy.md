# gauravxsuvo/DeepDarcy

⭐ 18 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/gauravxsuvo/DeepDarcy) · 个人维护

**PINN 预测地下水枯竭并反演未上报抽水率的全栈应用**

基于 PyTorch 的物理信息神经网络（PINN）：通过自动微分直接求解地下水流动方程（含二阶扩散导数），同时从稀疏井位观测反演空间变化的地层枯竭率（逆问题），并在美国堪萨斯 Ogallala 含水层真实 USGS 井数据上训练验证。以 FastAPI 提供模型 REST 服务，Next.js+Leaflet 前端做地图展示，Docker Compose 一键运行，前端与 API 均展示模型不确定性。README 明确其为研究/作品集产出而非校准的水管理工具，真实数据留出误差为 38.3% 相对 L2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch autograd 实现 PDE 残差损失（含二阶导），验证于 Theis 解析解（0.91% 相对 L2）
- 逆问题：从稀疏噪声观测反演空间变化的抽水/枯竭率（合成数据 5.15% 相对误差）
- FastAPI + Next.js/Leaflet 全栈部署，每次请求均展示模型不确定性
- 提供 model card 记录训练数据、指标与已知局限

## 适用场景

- 学习物理信息机器学习的端到端示例（PDE 残差、逆问题、过拟合检测）
- 获取 Ogallala 含水层区域地下水枯竭趋势的量级估计
- 了解科学模型通过 REST API 与地图前端服务化的做法

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: A physics-informed neural network (PINN) that predicts groundwater
> L13: trains a neural network that solves the governing groundwater flow
> L42: - Solving an inverse problem: recovering an unknown physical parameter

## 星数曲线

```mermaid
xychart-beta
    title "gauravxsuvo/DeepDarcy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c06289e51185` · [字段定义](../../DATASET.md)*
