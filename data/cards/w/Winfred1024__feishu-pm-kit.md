# Winfred1024/feishu-pm-kit

⭐ 30 · Python · MIT · 推送 2026-05-25 · [GitHub](https://github.com/Winfred1024/feishu-pm-kit) · 个人维护 · 中文 README

**可部署到飞书的 AI 项目经理 Agent 与项目管理系统套件**

将「Claude Code + CLAUDE.md 操作手册 + lark-cli 飞书通道」模式产品化的部署套件：共享引擎驱动多团队实例，新团队加一份 config 并跑 bootstrap 即上线。Agent 在飞书业务群监听消息、@责任人、识别风险、发日报；项目档案以 markdown frontmatter 为唯一事实源，脚本生成索引与健康看板并做四项治理校验，可单向镜像到飞书多维表格。依赖 Python 3.10+ 与 @larksuite/cli。Phase 5（真实实例迁移与多维表格联调）标注为未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 共享引擎 + 多实例配置，团队差异全部进 config.yaml，引擎零硬编码
- markdown frontmatter 为唯一事实源，索引生成 + 四项治理校验（必填/一致性/新鲜度/编号）
- 支持单向镜像到飞书多维表格与日报/风险识别等 Agent 行为
- TDD 开发，22 个测试通过

## 适用场景

- 为多个团队快速部署各自的飞书 AI 项目经理
- 以 markdown 管理项目档案并自动生成健康看板与治理报告
- 把项目状态同步到飞书多维表格供团队查看

## 场景标签

`聊天机器人` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: 把"**Claude Code 本体 + `CLAUDE.md` 操作手册 + `lark-cli` 飞书通道**"这一已验证的 AI 项目经理模式产品化:
> L15: - **Agent 项目经理**:在飞书业务群里监听消息、@责任人跟进、识别风险、发日报。Agent 本体是 Claude Code,在实例目录启动即加载该实例的 `CLAUDE.md`,化身那个团队的项目经理。

## 星数曲线

```mermaid
xychart-beta
    title "Winfred1024/feishu-pm-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `40e7a4f518ca` · [字段定义](../../DATASET.md)*
