# kmontag/macher

⭐ 160 · Emacs Lisp · GPL-3.0 · 推送 2026-10-02 · [GitHub](https://github.com/kmontag/macher) · 个人维护

**Emacs 的项目感知多文件 LLM 编辑工具集（基于 gptel）**

构建于 gptel 之上的 Emacs 编辑工具集：为 LLM 提供在当前项目内读取、搜索、编辑文件的工具，修改先在内存中捕获并以补丁（diff）形式展示，用户审阅后按块应用或发回修订。提供 6 个内置预设（如 @macher 全功能、@macher-ro 只读）与 implement/revise/discuss 动作命令；文件操作限制在 project/file（可选 directory）工作区内。适用于任何支持工具调用的 gptel 后端。通过 MELPA 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 编辑以补丁形式在内存中捕获，审阅后才写入磁盘
- 内置 8 种文件工具（读/搜索/编辑/写入/移动/删除等）
- 预设与动作命令体系（implement/revise/discuss），可自定义扩展
- 文件操作限制在可配置的工作区范围内

## 适用场景

- 在 Emacs 中让 LLM 实现跨多文件的项目修改并先审阅补丁
- 以只读预设向 LLM 提问项目相关代码
- 伪代理式工作流：让 LLM 调用工具做研究再产出聚合修改

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A project-aware LLM editing toolset for Emacs, built on gptel.
> L14: Aider or Plandex. It works with any gptel backend that

## 星数曲线

```mermaid
xychart-beta
    title "kmontag/macher 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 158 --> 161
    line [159, 160, 160]
```

2026-10-18 159 → 2026-10-25 160（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e7462d1ede2e` · [字段定义](../../DATASET.md)*
