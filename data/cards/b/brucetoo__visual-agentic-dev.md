# brucetoo/visual-agentic-dev

⭐ 102 · TypeScript · NOASSERTION · 推送 2026-02-14 · [GitHub](https://github.com/brucetoo/visual-agentic-dev) · 个人维护

**浏览器内点击定位元素并交给 AI agent 修改的沉浸式开发环境**

面向 React 开发者的浏览器开发环境：通过 React Fiber 机制零配置定位页面元素对应源码位置，用户选中元素后在聊天框描述修改需求，由已配置的编码 agent（如 Claude Code、CCR）在集成的持久化终端中执行修改，形成点击定位+agent 编辑的闭环。架构上由 Chrome 扩展、npm 全局安装的 bridge server（vdev-server）和 react-devtools SDK 三部分组成；React 19+ 需额外配置构建插件恢复 _debugSource 能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 React Fiber 的零配置源码定位，不向业务代码插入冗余属性
- 动态 agent 注册机制，支持 Claude Code、CCR 等多种 agent 并自动检测就绪状态
- 多项目并行开发：按 Tab 自动识别项目并切换终端会话
- 支持多选页面元素批量发送给 agent 修改

## 适用场景

- 在浏览器里点选页面元素，用自然语言让编码 agent 完成修改
- 同一浏览器中并行开发多个 React 项目并保持各终端会话
- 对多个页面元素批量描述需求，由 agent 一次性修改

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **Visual Agentic Dev** is an immersive browser development environment designed to allow developers to complete code
> L11: - 🤖 **Dynamic Agent Registry**: Extensible architecture supporting multiple AI agents (Claude Code, CCR, etc.) with
> L116: 3. Select your preferred agent (e.g., `ccr code` or `claude`).

## 星数曲线

```mermaid
xychart-beta
    title "brucetoo/visual-agentic-dev 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 101 --> 104
    line [103, 102, 102]
```

2026-10-18 103 → 2026-10-27 102（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `dafc6cdf0d89` · [字段定义](../../DATASET.md)*
