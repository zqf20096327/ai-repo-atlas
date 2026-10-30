# jithin-jz/ClashCode

⭐ 16 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/jithin-jz/ClashCode) · [官网](https://clash.jithin.site) · 个人维护

**游戏化编程学习平台：闯关练代码，AI 导师辅助**

ClashCode 是一个以关卡闯关方式学习与练习编程的 Web 平台：用户解题解锁关卡、在数字世界中推进，配套全局实时聊天与基于 RAG 的 AI 导师（上下文提示与自动代码分析）。技术栈为 React 19 前端 + FastAPI/Django/Celery 后端，部署于 Amazon EKS，数据层使用 PostgreSQL、DynamoDB、Pinecone、Redis。不可信代码在每次运行的资源受限沙箱进程（生产环境 gVisor、无网络、deny-all egress）中执行，通过可信测试框架与 per-run token 判定过关。README 未给出本地安装运行命令，仅 MIT 许可声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 关卡制游戏化编程学习与服务器端关卡解锁
- RAG 型 AI 导师：上下文提示与自动代码分析
- 每次运行使用干净资源受限沙箱进程（gVisor、无网络、rlimits）
- EKS 分布式部署，Prometheus 集群遥测与健康诊断

## 适用场景

- 通过闯关方式练习编程并获得 AI 提示
- 在实时聊天社区中与其他学习者交流
- 在沙箱中安全运行不可信用户代码并自动判题

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: ClashCode is a fun, game-like platform where you can learn and practice coding. Instead of just reading text, you so
> L9: * **🤖 AI-Powered Mentorship**: RAG-based AI tutor providing contextual hints and automated code analysis.

## 星数曲线

```mermaid
xychart-beta
    title "jithin-jz/ClashCode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `5a2f587648be` · [字段定义](../../DATASET.md)*
