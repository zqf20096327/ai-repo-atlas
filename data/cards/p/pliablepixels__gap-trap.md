# pliablepixels/gap-trap

⭐ 181 · JavaScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/pliablepixels/gap-trap) · [官网](https://pliablepixels.github.io/gap-trap/) · 个人维护

**为 AI 编码 agent 仓库生成规则与提交门禁的技能**

安装到 Claude Code / Codex 技能目录的 agent skill：在仓库中运行 setup 后读取代码，为每条适配该代码库的规则生成一个门禁（gate），规则被违反时使 commit 或 CI 失败，agent 无法跳过。机制包括 Contracts（HTTP/日志/认证等唯一正确写法）、Proven red（新测试对旧代码应失败）、Ratchets（已知问题计数只降不升）与 Playbooks。Node/Python 在测试套件内置门禁，其他语言用 git/grep/awk shell 版本。要求运行在较高档模型（Opus 或同级）并建议人工校验生成的规则。

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

- 读取代码库后生成规则并为每条规则添加 commit/CI 门禁
- 四类机制：Contracts、Proven red、Ratchets、Playbooks
- 支持任意语言：Node/Python 走测试套件，其余用 git/grep/awk shell 脚本
- 附带安装 slop-mop 技能以规范文档与提交信息

## 适用场景

- 我让 agent 写大部分代码，希望有机制阻止质量漂移
- 把团队经验固化为可执行的门禁而非纯文本指令
- 定期 refine 检出无门禁的规则与失效契约

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L23: Run it once in a repository. It reads the code, writes the rules that
> L25: fails the commit or the CI run when the rule is broken. The agent cannot
> L57: Or by hand. Claude Code reads `~/.claude/skills`, Codex reads

## 星数曲线

```mermaid
xychart-beta
    title "pliablepixels/gap-trap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 180 --> 182
    line [181, 181]
```

2026-10-18 181 → 2026-10-30 181（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6e99fd19f309` · [字段定义](../../DATASET.md)*
