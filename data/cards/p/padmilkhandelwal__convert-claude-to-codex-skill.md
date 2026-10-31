# padmilkhandelwal/convert-claude-to-codex-skill

⭐ 15 · MIT · 推送 2026-05-05 · [GitHub](https://github.com/padmilkhandelwal/convert-claude-to-codex-skill) · 个人维护

**将 Claude 技能自动转换为 Codex CLI 可用技能的工具**

面向 Codex CLI 用户的技能迁移工具：在 marketplace 中按名搜索 Claude 技能，抓取后逐行映射工具调用差异（TodoWrite→checklist、Bash tool→shell、Task tool→spawn_agent 等），重写 frontmatter，生成必需的 agents/openai.yaml 元数据，并写入 .codex/skills/ 目录。支持 --dry-run 预览、--global 全局安装、--multi-agent 三子代理流水线与 --test 独立验证代理。以 SKILL.md 技能形式分发，通过 git clone 安装。

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

- 搜索→抓取→转换→验证→安装一条命令完成
- Claude→Codex 工具调用逐行映射与 frontmatter 重写
- 自动生成 agents/openai.yaml 元数据
- --multi-agent 模式下独立 Tester 代理做冷读验证

## 适用场景

- 把常用的 Claude 技能搬到 Codex CLI 中继续使用
- 批量转换多个技能并全局安装
- 转换前用 --dry-run 预览工具替换效果

## 场景标签

 · 领域:AI 开发者工具/agent 技能

## 证据(README 行号)

> L9: Claude and Codex skills share a similar structure, but small differences in tool naming and configuration can break 
> L22: `$claude-to-codex` handles every substitution automatically, rewrites

## 星数曲线

```mermaid
xychart-beta
    title "padmilkhandelwal/convert-claude-to-codex-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ee48305b6eb6` · [字段定义](../../DATASET.md)*
