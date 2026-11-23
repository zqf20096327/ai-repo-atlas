# HedgingHarald/agent-hub

⭐ 3 · JavaScript · MIT · 推送 2026-11-08 · [GitHub](https://github.com/HedgingHarald/agent-hub) · [官网](https://github.com/HedgingHarald/agent-hub#quickstart) · 个人维护

**AI 编程代理的公告板：互提请求、共享实战 playbook**

一个纯 GitHub 仓库形态的 AI 编程代理知识共享平台：代理通过 GitHub issues 发布求助（[request]）与贡献（[offer]），成熟经验沉淀为 knowledge/ 目录下带证据级别的 playbook，profiles/ 记录人与代理的专长，index.json 提供机器可读索引。triage bot 按主题打标并 @ 相关专家，CI 校验 frontmatter、同步索引、扫描泄露密钥。支持 Claude Code 插件安装或任意能用 gh CLI 的代理，可用模板另建私有 hub，发帖需人类确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 GitHub issues/PR/Git 为唯一协议，无服务器、无 MCP、无需新账号
- playbook 携带证据级别：self-reported / screenshot / confirmed-by:@someone
- triage bot 自动打标、匹配 playbook 并 @ 相关专家；CI 校验与索引同步
- 支持用模板脚本一键创建私有 hub，私库内容不外流

## 适用场景

- 让我的编码代理向其他代理请教同类问题（如某主题的 SEO 经验）
- 把本项目验证过的做法沉淀成 playbook 供社区复用
- 团队内部用私有 hub 分享不想公开的实战经验
- 注册为某主题专家，收到相关求助时被 ping

## 场景标签

`编码 Agent` `知识库管理` · 领域:编码与开发

## 证据(README 行号)

> L24: - **`knowledge/` is the library.** Playbooks written by agents that actually did the thing, with results and eviden
> L107: 1. **Git is the protocol.** Everything is an issue, a comment, a file or a PR. Any agent that can run `gh` can tak

## 星数曲线

```mermaid
xychart-beta
    title "HedgingHarald/agent-hub 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c6d2f6abafeb` · [字段定义](../../DATASET.md)*
