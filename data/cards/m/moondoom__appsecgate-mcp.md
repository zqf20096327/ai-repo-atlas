# moondoom/appsecgate-mcp

⭐ 3 · Python · MIT · 推送 2026-11-07 · [GitHub](https://github.com/moondoom/appsecgate-mcp) · [官网](https://moondoom.github.io/appsecgate-mcp/) · 个人维护

**给 AI 编码代理用的本地离线安全扫描 MCP 服务器**

以 MCP 服务器形式运行的安全扫描工具，在 Claude Code、Cursor、Cline、Continue 四类客户端内扫描文件、git diff 与整个项目，离线运行且代码不出本机。提供 17 个工具：扫描、指纹去重与跨扫描跟踪、修复上下文获取（get_fix_context）、修复验证（verify_fix）、结果查询与导出、误报反馈与抑制。内置 Semgrep（SAST）、Gitleaks/TruffleHog（密钥）、Trivy（SCA）三个扫描器，项目以只读方式挂载，容器无网络权限。集中式 CI 与主从同步为独立部署，GUI 工单面板与 ASOC 集成未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个 MCP 工具覆盖扫描、修复上下文、修复验证与结果管理
- 默认离线：容器 --network=none、项目只读挂载、无 LLM 调用
- 内置 Semgrep/Gitleaks/TruffleHog/Trivy 扫描器，规则离线捆绑
- 发现按指纹去重，跨扫描跟踪，支持误报反馈与本地抑制

## 适用场景

- 让 AI 代理在每次 diff 落地前自动做安全扫描
- 离线环境下扫描代码，代码不出本机
- 让代理获取漏洞修复上下文并验证修复结果
- 本地跟踪去重后的安全发现，而非堆积报告

## 场景标签

`编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L9: AI agents ship code faster than security can review it. AppSecGate is an MCP
> L156: |SAST|Semgrep|Bundled offline rules (Rules Bundle) — no registry access needed|
> L166: - **Read-only project.** The project is mounted `:ro`; the server never writes to source files.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `9a1c110ada80` · [字段定义](../../DATASET.md)*
