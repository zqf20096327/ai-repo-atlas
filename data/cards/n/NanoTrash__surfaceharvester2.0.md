# NanoTrash/surfaceharvester2.0

⭐ 28 · Python · NOASSERTION · 推送 2026-11-15 · [GitHub](https://github.com/NanoTrash/surfaceharvester2.0) · 个人维护

**攻击面收集与漏洞扫描的 CLI 编排工具，结果存 SQLite**

面向渗透测试人员的命令行工具，按 Subfinder→Nmap→Nuclei→Gobuster 顺序编排外部扫描器，发现子域名、端口、CVE、misconfig、目录与联系人信息，通过 vulnx 检索 CVE 对应的公开利用。结果去重后存入 SQLite，支持按目标、严重性、会话等维度生成文本与 JSON 报告，并记录 Nuclei 的 template-id、matcher-name 等证据。处理联系人等文本时使用 spaCy 模型与 NLTK 数据（首次运行自动下载）。提供一键安装脚本与 Poetry 手动安装两条路径，需 Linux/WSL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编排 Subfinder/Nmap/Nuclei/Gobuster 完成子域名→端口→漏洞→目录扫描流水线
- 结果存 SQLite，含会话历史、去重与自动迁移
- vulnx 检索 CVE 公开利用并缓存结果
- 文本处理使用 spaCy en_core_web_sm 与 NLTK 数据（可自动下载）

## 适用场景

- 对自有授权目标做一站式攻击面收集与漏洞扫描
- 按目标/严重性/会话导出扫描报告
- 对已发现 CVE 查找公开利用代码

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: SurfaceHarvester 2 — CLI-инструмент для сбора поверхности атаки и поиска уязвимостей веб-приложений и сетевых сервис
> L15: - извлечение email и телефонов со стартовой страницы;

## 星数曲线

```mermaid
xychart-beta
    title "NanoTrash/surfaceharvester2.0 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-18"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-11-15 28 → 2026-11-18 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `924d92d6ec27` · [字段定义](../../DATASET.md)*
