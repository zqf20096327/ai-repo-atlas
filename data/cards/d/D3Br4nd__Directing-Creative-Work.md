# D3Br4nd/Directing-Creative-Work

⭐ 4 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/D3Br4nd/Directing-Creative-Work) · [官网](https://www.debrandstudio.it) · 个人维护

**让 AI agent 在创意文案中主动选择创作方向的技能**

以 Agent Skill 形式分发的一组纯指令（无脚本、无网络、无依赖），可装载进 Claude Code、OpenAI Codex、OpenCode、Google Antigravity 等支持 Skills 规范的 agent。技能机制：先识别简报中最可预测的处理方式与'第一机巧转折'，再在简报中寻找能改变创作本身的细节，据此选择创作方向；输出交付物优先，附最多三条方向说明与待确认事实。含各媒介默认套路清单、多语言支持与评测用例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯指令实现：无脚本、无网络、无 API key、无依赖
- 先列出可预测版本再选择创作方向，交付物优先于方向说明
- 支持 Claude Code / Codex / OpenCode / Antigravity 及 claude.ai 自定义技能
- 附五语激活查询与 evals.json 测试用例

## 适用场景

- 让 agent 写广告语、落地页文案时避免通用套路
- 改写银行 App 等功能性消息并保留错误码等事实
- 为产品起名、写视频脚本时给出多个可选方向

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L43: No setup, no dependencies, no API keys: the skill is pure instructions. Other install options are below.
> L192: None. The skill contains only instructions: no scripts, no network, no packages.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `dcb0285e9659` · [字段定义](../../DATASET.md)*
