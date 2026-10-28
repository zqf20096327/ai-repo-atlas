# baidu-maps/stability-analysis-agent

⭐ 50 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/baidu-maps/stability-analysis-agent) · 组织维护 · 中文 README

**App 稳定性 Agent：从 Crash/ANR/OOM 日志定位根因并自动修复代码**

面向 App 稳定性工程的开源领域 Agent：解析 Crash/ANR/OOM 等日志，结合符号文件完成堆栈地址符号化与源码定位，基于故障地址、寄存器、调用关系构建证据链，输出含三级根因定位、置信度与修复建议的分析报告，并直接修改源码（保留原文件备份，可用 git diff 审查）。覆盖 iOS/macOS/Android/鸿蒙/Linux/Windows 平台，通过规则与向量数据库沉淀历史案例，支持 Tool/Workflow/Skill 扩展及修复后的测试验证闭环。以 pip 包与交互式 CLI 提供，需用户自行配置大模型与符号化工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 日志解析→符号化→证据链→源码定位→AI 修复的完整链路
- 覆盖 iOS/macOS/Android/鸿蒙/Linux/Windows 六平台 Crash 分析
- 生成含三级根因定位、证据链、置信度与修复建议的报告
- Tool/Workflow/Skill 扩展机制与修复后构建测试验证闭环

## 适用场景

- 拿到 Crash 日志后自动符号化并定位根因与责任代码
- 让 Agent 生成并落地代码修复，再用 git diff 审查
- 通过相似案例检索复用历史稳定性问题的分析经验

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **一个面向 App 稳定性工程的开源领域 Agent：以受治理的 Agent Harness 为运行底座，借鉴开源 AI 编程工具在上下文管理、多轮调查、工具调用、权限控制、检查点恢复与验证闭环等方面的能力，将 Crash、ANR
> L19: |崩溃位置不一定是根因|容易根据表面堆栈生成猜测|结合故障地址、寄存器、调用关系等信息构建 Crash 证据链|
> L125: 当前内置 Crash 分析链路覆盖 iOS、macOS、Android、鸿蒙、Linux 和 Windows，统一完成日志解析、堆栈符号化、证据分析、源码上下文提取和 AI 修复。不同平台通过对应的日志解析器和符号化工具接入，具

## 星数曲线

```mermaid
xychart-beta
    title "baidu-maps/stability-analysis-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d0d41b4e9a89` · [字段定义](../../DATASET.md)*
