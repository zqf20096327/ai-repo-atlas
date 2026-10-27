# anilcancakir/laravel-ai-sdk-skills

⭐ 26 · PHP · MIT · 推送 2026-09-13 · [GitHub](https://github.com/anilcancakir/laravel-ai-sdk-skills) · [官网](https://medium.com/@anilcan/level-up-your-laravel-ai-agents-with-modular-skills-39da3fe9fe4b) · 个人维护

**Laravel AI SDK 的技能系统：以 SKILL.md 模块化定义 AI agent 能力**

扩展 Laravel AI SDK 的 PHP Composer 包，为 AI agent 提供可复用技能模块机制：每个技能是一个含 YAML frontmatter 的 SKILL.md 文件，封装指令与工具。通过渐进披露（Progressive Disclosure），agent 先看到技能列表与简短描述，按需加载完整内容，以控制上下文窗口占用。提供 Skillable trait、list_skills/skill/skill_read 内置工具、lite/full 两种注入模式、技能发现缓存、声明式授权与面向前缀缓存的提示词组织辅助。要求 PHP 8.3+ 与 Laravel 12/13，自动注册服务提供者，附 Artisan 脚手架命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md + YAML frontmatter 定义技能，渐进披露按需加载
- lite/full 两种注入模式，支持按技能覆盖全局 discovery_mode
- enforce_declared 声明式授权，限制 agent 可访问的技能范围
- withSkillInstructions 按静态→技能→动态排序组织提示词以利前缀缓存

## 适用场景

- 把 Laravel AI SDK agent 的能力拆成独立技能文件维护
- 控制大量技能下的上下文窗口占用
- 为不同 agent 声明各自可用的技能子集

## 场景标签

`Agent 框架` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10: This package extends the Laravel AI SDK with a high-performance skill system. Skills are reusable capability module
> L24: |`laravel/ai`|`>=0.7 <0.12`, installed for you as a runtime dependency|

## 星数曲线

```mermaid
xychart-beta
    title "anilcancakir/laravel-ai-sdk-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7c005813b2f1` · [字段定义](../../DATASET.md)*
