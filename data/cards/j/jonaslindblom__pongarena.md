# jonaslindblom/pongarena

⭐ 4 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/jonaslindblom/pongarena) · [官网](https://jonaslindblom.github.io/pongarena/) · 个人维护

**浏览器中的微型神经网络 Pong 对战与可解释性实验场**

一个在浏览器中运行的 Pong 对战实验平台：用户提供鼠标/键盘控制或导入自己的 ONNX 权重，与程序化、提示生成、强化学习训练三类神经网络控制器对战或观赛。提供实时神经元激活查看、逐个关闭神经元观察决策变化、模型卡与联赛积分榜。内置 8 个模型（13 到 50,819 参数），模型经 PR 提交后由 CI 验证并生成对局结果。本地运行需 Node.js，训练需 Python。

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

- 比较 programmed、prompted、trained 三种权重来源，共享同一 163 参数架构
- 实时查看神经元激活并可关闭单个神经元观察决策变化
- 接受社区 ONNX 模型提交，CI 自动验证图结构与资源预算
- 联赛使用 512 组共享发球集，28,672 局可复现对局

## 适用场景

- 和微型神经网络打 Pong 并观察其激活
- 导入自己的 ONNX 模型参加联赛
- 教学演示小型网络的可解释性

## 场景标签

`强化学习` `模型评测` `教程课程` · 领域:评测与运维

## 证据(README 行号)

> L5: Play against tiny neural networks, watch their neurons fire, or switch one off to see what changes. This open-source
> L15: **Quill, Small and OneShot share the same 163-parameter ReLU network: `6 → 12 → 4 → 3 → 3`.** Quill's programmed we

## 星数曲线

```mermaid
xychart-beta
    title "jonaslindblom/pongarena 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-19", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-18 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0fa04401affe` · [字段定义](../../DATASET.md)*
