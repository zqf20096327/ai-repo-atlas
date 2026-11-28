# toxy4ny/php2shell-checker

⭐ 4 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/toxy4ny/php2shell-checker) · 个人维护

**给 Debian 12/13 服务器做 PHP/Brotli 包漏洞只读审计**

面向 Debian 12/13 的只读包审计脚本：盘点 PHP 核心包（FPM/CLI/CGI/mod_php）与 Brotli 库的 dpkg 版本，对照内嵌的 CVE 修复阈值逐 CVE 输出 FIXED/UPDATE/UNKNOWN/REVIEW 判定，并读取 procfs 检查运行进程的过期 PHP 文件证据；产出文本或 JSON 报告与区分组件的退出码，不安装包、不执行 PHP、不发起网络请求。附带 SKILL.md 供 AI agent 注册并引导其在目标主机上运行与解读结果。规则为 2026-10-23 校验、内嵌于脚本，不自动刷新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐 CVE 报告（CVE-2026-109618/109619/111497），独立 Brotli 组件判定
- 读取 procfs 检查运行进程的 stale PHP 文件与重启证据，不执行 PHP、不读进程内存
- JSON stdout 单文档 schema 1.1，含分组件退出码与建议命令参数数组（不执行）
- SKILL.md agent 技能文件，可被 skill loader 注册以引导审计与结果解读

## 适用场景

- 审计 Debian 12/13 服务器上 PHP 包是否低于已知修复版本
- 检查运行中 PHP/FPM 进程是否存在需重启的过期文件证据
- 让 AI agent 按 SKILL.md 在目标主机执行只读漏洞检查并解读 JSON 报告
- 自动化管道中按 summary.package_exit_code 等分项退出码做告警

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: A read-only PHP and Brotli package audit for **Debian 12 (bookworm)** and **Debian 13 (trixie)**.
> L56: ## Using with AI agents
> L58: The repository includes an agent skill at SKILL.md, named

## 星数曲线

```mermaid
xychart-beta
    title "toxy4ny/php2shell-checker 星数(近 3 点)"
    x-axis ["2026-11-12", "2026-11-19", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-12 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `b16e769e450b` · [字段定义](../../DATASET.md)*
