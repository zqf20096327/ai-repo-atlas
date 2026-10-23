# habit-hooks/habit-hooks

⭐ 232 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/habit-hooks/habit-hooks) · [官网](http://habit-hooks.com/) · 组织维护

**把 linter 违规改写为辅导指南、引导 AI 编程代理改进代码的工具**

面向使用 AI 编程代理的开发者的质量检查工具：运行 ruff、eslint、jscpd 等检测器，把原始规则违规翻译成工具无关的 smell key（如 too-many-parameters），再渲染成代理可执行的短辅导指南，替代长规则文档。由 habit-sensors 与 habit-mapper 两个管道命令组成，支持 Python/TypeScript/PHP/Java/Ruby 插件，可按分支/提交范围扫描、snooze 存量问题、以退出码区分发现与故障。需 Python 3.11+，检测器需另行安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- linter 违规映射为工具无关的 smell key 并输出辅导指南
- habit-sensors | habit-mapper 管道架构，可独立运行与替换
- 支持 Python/TypeScript/PHP/Java/Ruby 五种语言插件（opt-in extras）
- 退出码区分 enforced 发现（1）与工具故障（2），便于 CI 包装

## 适用场景

- 让 AI 编程代理在编码时收到可执行的改进建议而非原始 linter 报错
- 在 CI 中对分支改动做结构异味检查并阻断未修复的提交
- 存量代码库先 snooze 旧问题、只跟踪新增异味

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: Stop reciting software engineering literature to your AI agent. Habit Hooks runs your linters, then replaces
> L22: - Habit Hooks supplies the missing loop from outside. The linter finding is the cue; the coaching guide is
> L253: habit-sensors <scope flags> | habit-mapper

## 星数曲线

```mermaid
xychart-beta
    title "habit-hooks/habit-hooks 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 226 --> 233
    line [227, 228, 232]
```

2026-10-18 227 → 2026-10-23 232（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b231b3d03166` · [字段定义](../../DATASET.md)*
