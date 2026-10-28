# ouka-lab/untodo

⭐ 36 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/ouka-lab/untodo) · [官网](https://ouka-lab.github.io/untodo/) · 个人维护 · 中文 README

**给开发者与 AI 编程助手的类型安全 TODO 函数库**

用函数调用 TODO()/FIXME()/HACK() 替代 // TODO: 注释的 TypeScript 库。函数返回 never，类型系统可检测未实现路径；调用时传入 reason/issue/assignee 等结构化元数据，可通过声明合并扩展字段；配套 ESLint/oxlint 插件以 no-todo 等规则在 CI 阻断构建。设计动机之一是 AI 编程助手能从类型与函数签名中识别 TODO 的存在与意图。运行时约 1.4 KB，支持以别名替换为空实现消除开销。npm 安装，npx untodo init 生成配置。

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

- TODO/FIXME/HACK 函数返回 never，类型系统可检测未实现代码
- 结构化元数据（reason/issue/assignee 等）且支持声明合并扩展
- ESLint/oxlint 插件提供 no-todo/no-fixme/no-hack 规则
- 可通过 bundler 别名替换为空实现，消除生产包运行时

## 适用场景

- 让 AI 编程助手可靠识别代码中的 TODO 及其上下文
- 用 lint 在 CI 阻断遗留的注释式 TODO
- 团队统一 TODO 书写格式并接入日志处理

## 场景标签

 · 领域:软件开发工具

## 证据(README 行号)

> L35: ## Affinity with AI coding assistants
> L43: A `TODO` in untodo is a function call backed by a type definition. AI coding assistants (Claude, GitHub Copilot, et
> L17: Type-safe replacement for `// TODO:` comments. Type-safe TODO for AI coding. AI agent TODO.

## 星数曲线

```mermaid
xychart-beta
    title "ouka-lab/untodo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-28 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d8324202b57e` · [字段定义](../../DATASET.md)*
