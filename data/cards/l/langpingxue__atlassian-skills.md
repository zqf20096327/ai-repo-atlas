# langpingxue/atlassian-skills

⭐ 41 · Python · 推送 2026-04-10 · [GitHub](https://github.com/langpingxue/atlassian-skills) · [官网](https://medium.com/@xuelangping/introducing-atlassian-skills-extending-ai-agent-with-atlassian-integration-fa19f6056df7) · 个人维护

**Claude Code 的 Atlassian 集成技能：操作 Jira/Confluence/Bitbucket**

面向 Claude Code 的技能（SKILL.md 文件夹），使 Claude 能直接操作 Jira、Confluence、Bitbucket：包括 issue 增删改、JQL 搜索、冲刺管理、Confluence 页面与评论、Bitbucket 仓库与 PR 等共 45 个方法。提供完整读写与只读两种变体，支持 Cloud（API Token）与 Data Center（PAT）双认证；Data Center 已实测，Cloud 未验证。安装方式为复制技能目录并 pip 安装依赖，含 203 个测试用例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Jira/Confluence/Bitbucket 共 45 个方法（读写与只读两变体）
- Cloud（API Token）与 Data Center（PAT）双认证
- 统一 JSON 返回格式与六类错误类型
- 包含 203 个测试用例

## 适用场景

- 在 Claude Code 中用自然语言创建和搜索 Jira issue
- 让 Claude 检索和编辑 Confluence 页面
- 通过对话操作 Bitbucket 仓库与合并 PR

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A Claude Code skill for integrating with Jira, Confluence, and Bitbucket. Supports both Cloud and Data Center deploy
> L9: Skills are folders containing a `SKILL.md` file that teach Claude Code new capabilities. When you add this skill to 

## 星数曲线

```mermaid
xychart-beta
    title "langpingxue/atlassian-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-26 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fd1f83f0bb1c` · [字段定义](../../DATASET.md)*
