# Koukyosyumei/AIJack

⭐ 429 · C++ · Apache-2.0 · 推送 2026-05-30 · [GitHub](https://github.com/Koukyosyumei/AIJack) · [官网](https://koukyosyumei.github.io/AIJack/) · 个人维护

**给机器学习研究者的安全与隐私风险模拟库**

面向 ML 模型的安全与隐私风险仿真工具：以 Python API 形式提供 Attacker 接口模拟投毒、模型反演、后门、Free-Rider、成员推断等攻击，以及差分隐私、同态加密、K-匿名、联邦学习等防御方法，共支持 30 余种算法；对分布式学习提供 Client/Server/API/Manager 四类抽象，C++ 后端与 MPI 后端加速，兼容 PyTorch 与 scikit-learn。附带 SQL 式 ML 调试数据库 AIValut（限研究用途）。安装需 Boost 与 pybind11，提供 Dockerfile。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 余种攻击/防御算法（投毒、模型反演、FGSM、DPSGD、Paillier 等）
- 联邦/分割学习的 Client/Server/API/Manager 模块化接口
- PyTorch 友好、兼容 scikit-learn，C++ 与 MPI 后端
- 附带 SQL 式 ML 调试 DBMS AIValut

## 适用场景

- 仿真测试我的模型对投毒或反演攻击的脆弱性
- 在联邦学习实验中对比差分隐私、鲁棒聚合等防御
- 用 SQL 式查询训练并调试 ML 模型（AIValut）

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: AIJack is an easy-to-use open-source simulation tool for testing the security of your AI system against hijackers. I
> L44: For standard machine learning algorithms, AIJack allows you to simulate attacks against machine learning models wit
> L62: For distributed learning such as Federated Learning and Split Learning, AIJack offers four basic APIs: `Client`, `S

## 星数曲线

```mermaid
xychart-beta
    title "Koukyosyumei/AIJack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 428 --> 430
    line [429, 429]
```

2026-10-18 429 → 2026-10-30 429（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `eac91c1b0ff3` · [字段定义](../../DATASET.md)*
