# bitsky-tech/bridgic-agent

⭐ 50 · TypeScript · AGPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/bitsky-tech/bridgic-agent) · 组织维护 · 中文 README

**本地优先的桌面通用 Agent 与自动化工作流构建器**

Bridgic Agent 是面向终端用户的本地优先桌面应用，含 Python 后端与 Electron 客户端。用户通过 /build 命令用自然语言描述目标，Agent 经 clarify→explore→generate→verify 阶段自动构建并验证可复用工作流；支持多子代理并行、秒级 cron 调度、内嵌 Chromium 浏览器自动化、基于能力的权限模型与 Git 检查点回滚。需在设置中配置模型 Provider 与凭据。限制：非多用户网关，非操作系统沙箱，自动长期记忆召回尚未实现。提供 macOS(.pkg)/Windows(.exe) 安装包或源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /build 命令将自然语言目标转化为可运行工作流，支持 200+ 轮探索
- 多子代理并行（每根会话最多 10 个）与秒级 cron 调度
- 内嵌 Electron 自有 Chromium 的浏览器自动化（经 CDP）
- Request/Auto/Full 三级权限模式与 Dulwich Git 检查点

## 适用场景

- 用自然语言描述目标让 Agent 自动构建自动化工作流
- 长期运行、调度和迭代演化私有自动化流程
- 让 Agent 操作浏览器完成表单填写与结果核验

## 场景标签

`工作流自动化` `浏览器自动化` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Bridgic Agent is a general-purpose, local-first desktop agent and an intelligent automation workflow builder. Design
> L13: Tell Bridgic Agent what you want. It explores, builds, and verifies the workflow. **No automation expertise needed.
> L17: You set the goal. Bridgic Agent figures out the path, drives the task forward. It can keep progressing toward a suc

## 星数曲线

```mermaid
xychart-beta
    title "bitsky-tech/bridgic-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f6200c3e2a20` · [字段定义](../../DATASET.md)*
