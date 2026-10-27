# merlinquantum/merlin

⭐ 37 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/merlinquantum/merlin) · [官网](https://merlinquantum.ai/) · 组织维护

**面向 AI 从业者的光子量子机器学习 PyTorch 框架**

基于 PyTorch 接口风格的光子量子机器学习框架：提供可嵌入任意 PyTorch 模型的高层量子层 API，底层封装光子架构选择、ansatz 设计、输入编码与光子数配置，并基于 Perceval 框架实现。以经典模拟为主，可连接 Quandela Cloud 等光子 QPU 远程平台；支持复现已发表论文与基准测试，GPU 模拟可扩展至 500+ 模式芯片。面向 AI/ML 从业者、量子研究者和企业团队，以 pip 包发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 高层 API 量子层可嵌入任意 PyTorch 模型，支持训练与推理
- 基于 Perceval，可连接光子 QPU（Quandela Cloud）
- GPU 优化模拟，扩展至 500+ 模式、10-20 光子
- 提供论文复现与基准测试工具（pytest-benchmark）

## 适用场景

- 在现有 PyTorch 模型中加入量子层构建混合模型
- 复现与基准测试已发表的量子机器学习论文
- 在真实光子量子处理器上实验量子算法

## 场景标签

 · 领域:量子计算/机器学习框架

## 证据(README 行号)

> L10: MerLin brings quantum computing capabilities to AI practitioners through easy-to-use PyTorch integrations. Named af
> L30: - **AI/ML Practitioners**: Add quantum layers to existing PyTorch models
> L111: import merlin as ML  # Package: merlinquantum, import: merlin

## 星数曲线

```mermaid
xychart-beta
    title "merlinquantum/merlin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9ff5b3059aa3` · [字段定义](../../DATASET.md)*
